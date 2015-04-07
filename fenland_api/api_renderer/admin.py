from django.core.urlresolvers import reverse
from django.utils.html import escape
from django.contrib import admin
from django.contrib.admin.models import LogEntry, DELETION
from api_renderer.models import Surgery, Volunteer, Status, Appointment, AuditLog


admin.site.index_title = 'Fenland Database'


class VolunteerInline(admin.TabularInline):
    model = Volunteer
    fields = ('surname', 'forenames', 'town', 'postcode', 'calculate_age')
    readonly_fields = ('surname', 'forenames', 'town', 'postcode',
                       'calculate_age')
    can_delete = False
    extra = 0
    def has_add_permission(self, request):
        return False


class SurgeryAdmin(admin.ModelAdmin):
    inlines = [VolunteerInline, ]

admin.site.register(Surgery, SurgeryAdmin)


class AppointmentInline(admin.TabularInline):
    model = Appointment
    fields = ('appt_date', 'appt_time', 'test_site')
    extra = 0


class VolunteerAdmin(admin.ModelAdmin):
    inlines = [AppointmentInline, ]
    search_fields = ('surname', 'forenames', 'town', 'postcode',
                     'surgeries__full_name')
    list_display = ('surname', 'forenames', 'town', 'postcode',
                    'calculate_age')
    list_filter = ('town', )
    date_hierarchy = 'dob'
    fieldsets = (
        (None, {'fields': (('surname', 'forenames'),
                           ('initials', 'dob'),
                           ('title', 'sex'))}),
        ('Address', {'classes': ('collapse',),
                     'fields': (('addr1', 'home_tel'), ('addr2', 'work_tel'),
                                ('town', 'mobile'), ('county', 'email'),
                                    'postcode')
                }
        ),
        ('Details', {'classes': ('collapse', 'extrapretty'),
                     'description': 'Extra <b>details</b>',
                     'fields': (('nhs_no', 'surgeries'),
                                ('modified', 'modified_by'),
                                ('diabetes_diagnosed', 'moved_away'),)}),
    )

admin.site.register(Volunteer, VolunteerAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('get_volunteer', 'appt_date', 'appt_time', 'test_site')
    search_fields = ('volunteers__surname', 'volunteers__forenames',)
    list_per_page = 5

    def get_volunteer(self, obj):
        return obj.volunteers

    get_volunteer.short_description = 'Volunteer'
    get_volunteer.admin_order_field = 'appointment__volunteer'

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
    object_link.admin_order_field = 'object_repr'
    object_link.short_description = u'object'
    
    def queryset(self, request):
        return super(LogEntryAdmin, self).queryset(request) \
            .prefetch_related('content_type')


admin.site.register(LogEntry, LogEntryAdmin)