from django.core.urlresolvers import reverse
from django.utils.html import escape
from django.contrib import admin
from django.contrib.admin.models import LogEntry, DELETION
from django.shortcuts import render
from api_renderer.models import Surgery, Volunteer, Status, Appointment, AuditLog
from import_export import resources
from import_export.admin import ImportExportModelAdmin
import arrow
import requests

admin.site.index_title = 'Fenland Database'


def my_view(request, *args, **kwargs):
    volunteers = Volunteer.objects.all()
    towns = {}
    appts = {}
    for v in volunteers:
        appts = v.appointment_set.count()
        if v.town not in towns.keys():
            towns[v.town] = {}
            towns[v.town]['t_count'] = 1
            towns[v.town]['a_count'] = appts
        else:
            towns[v.town]['t_count'] = towns[v.town]['t_count'] + 1
            towns[v.town]['a_count'] = towns[v.town]['a_count'] + appts
    return render(request, 'html_renderer/admin_view.html', {'towns': towns})

admin.site.register_view('somepath', view=my_view, urlname='somepath')


class VolunteerResource(resources.ModelResource):

    class Meta:
        model = Volunteer


class VolunteerInline(admin.TabularInline):
    model = Volunteer
    fields = ('town', 'postcode', 'calculate_age')
    readonly_fields = ('surname', 'forenames', 'town', 'postcode',
                       'calculate_age')
    can_delete = False
    extra = 0

    def has_add_permission(self, request):
        return False


class SurgeryAdmin(admin.ModelAdmin):
    inlines = [VolunteerInline, ]
    readonly_fields = ('modified', 'modified_by')
    fieldsets = (
        (None, {'fields': (('full_name', 'admin_contact_name'),
                           ('name', 'admin_contact_number'),
                           ('addr1', 'hscic_code'),
                           ('addr2', 'area'),
                           ('town',),
                           ('county'),
                           ('postcode'),
                           ('telephone'))}),
        ('Modified', {'fields': (('modified_by', 'modified'))})
    )

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user.get_username()
        obj.modified = str(arrow.now()).replace('+01:00', '')
        obj.save()

admin.site.register(Surgery, SurgeryAdmin)


class AppointmentInline(admin.TabularInline):
    model = Appointment
    fields = ('appt_date', 'appt_time', 'test_site')
    extra = 0


class VolunteerAdmin(ImportExportModelAdmin):
    resource_class = VolunteerResource
    readonly_fields = ('modified', 'modified_by')
    inlines = [AppointmentInline, ]
    search_fields = ('surname', 'forenames', 'town', 'postcode',
                     'surgeries__full_name')
    list_display = ('surname', 'forenames', 'town', 'postcode',
                    'calculate_age')
    list_filter = ('town', 'surgeries__full_name')
    # save_on_top = True
    date_hierarchy = 'dob'
    fieldsets = (
        (None, {'fields': (('surname', 'forenames'),
                           ('initials', 'dob'),
                           ('title', 'sex'))}),
        ('Address', {'classes': ('collapse',),
                     'fields': (('addr1', 'home_tel'), ('addr2', 'work_tel'),
                                ('town', 'mobile'), ('county', 'email'),
                                'postcode')}),
        ('Details', {'classes': ('collapse', 'extrapretty'),
                     'description': 'Extra <b>details</b>',
                     'fields': (('nhs_no', 'surgeries'),
                                ('modified', 'modified_by'),
                                ('diabetes_diagnosed', 'moved_away'),)}),
    )

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user.get_username()
        obj.modified = str(arrow.now()).replace('+01:00', '')
        requests.get('http://localhost:8080/model_update?user=%s&model=volunteer&name=%s' % (request.user.get_username(), obj.forenames + ' ' + obj.surname))
        obj.save()

admin.site.register(Volunteer, VolunteerAdmin)


class MyVolunteer(Volunteer):
    class Meta:
        proxy = True
        verbose_name = 'My Volunteer'
        verbose_name_plural = 'My Volunteers'


class VolunteerAdmin2(admin.ModelAdmin):
    inlines = [AppointmentInline, ]
    readonly_fields = ('modified', 'modified_by')
    search_fields = ('surname', 'forenames', 'town', 'postcode',
                     'surgeries__full_name')
    list_display = ('surname', 'forenames', 'town', 'postcode',
                    )
    list_filter = ('town', )
    date_hierarchy = 'dob'
    fieldsets = (
        (None, {'fields': (('surname', 'forenames'),
                           ('initials', 'dob'),
                           ('title', 'sex'))}),
        ('Address', {'classes': ('collapse',),
                     'fields': (('addr1', 'home_tel'), ('addr2', 'work_tel'),
                                ('town', 'mobile'), ('county', 'email'),
                                'postcode')}),
        ('Details', {'classes': ('collapse', 'extrapretty'),
                     'description': 'Extra <b>details</b>',
                     'fields': (('nhs_no', 'surgeries'),
                                ('modified', 'modified_by'),
                                ('diabetes_diagnosed', 'moved_away'),)}),
    )

    def get_queryset(self, request):
        qs = super(VolunteerAdmin2, self).get_queryset(request)
        # if request.user.is_superuser:
        #    return qs
        return qs.filter(modified_by=request.user)

admin.site.register(MyVolunteer, VolunteerAdmin2)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('get_volunteer', 'appt_date', 'appt_time', 'test_site')
    search_fields = ('volunteers__surname', 'volunteers__forenames',)
    list_per_page = 5
    date_hierarchy = 'appt_date'

    def get_volunteer(self, obj):
        return obj.volunteers

    get_volunteer.short_description = 'Volunteer'
    # get_volunteer.admin_order_field = 'appointment__volunteer'

admin.site.register(Appointment, AppointmentAdmin)


class AuditLogAdmin(admin.ModelAdmin):
    pass

admin.site.register(AuditLog, AuditLogAdmin)


class StatusAdmin(admin.ModelAdmin):
    pass

admin.site.register(Status, StatusAdmin)


class LogEntryAdmin(admin.ModelAdmin):

    date_hierarchy = 'action_time'

    # readonly_fields = LogEntry._meta.get_all_field_names()

    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_link',
        'action_flag',
        'change_message',
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser and request.method != 'POST'

    def has_delete_permission(self, request, obj=None):
        return False

    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = u'<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return link
    object_link.allow_tags = True
    # object_link.admin_order_field = 'object_repr'
    object_link.short_description = u'object'

    def queryset(self, request):
        return super(LogEntryAdmin, self).queryset(request) \
            .prefetch_related('content_type')


admin.site.register(LogEntry, LogEntryAdmin)
