from django.contrib import admin
from api_renderer.models import Surgery, Volunteer, Status, Appointment, AuditLog


admin.site.index_title = 'Fenland Database'


class VolunteerInline(admin.TabularInline):
    model = Volunteer
    fields = ('surname', 'forenames', 'town', 'postcode', 'calculate_age' )
    readonly_fields = ('surname', 'forenames', 'town', 'postcode', 'calculate_age' )
    can_delete = False


class SurgeryAdmin(admin.ModelAdmin):
    inlines = [ VolunteerInline, ]

admin.site.register(Surgery, SurgeryAdmin)


class AppointmentInline(admin.TabularInline):
    model = Appointment
    fields = ('appt_date', 'appt_time', 'test_site')


class VolunteerAdmin(admin.ModelAdmin):
    inlines=[AppointmentInline,]
    search_fields = ('surname', 'forenames', 'town', 'postcode', 'surgeries__full_name'  )
    list_display = ('surname', 'forenames', 'town', 'postcode', 'calculate_age' )
    list_filter = ('town',)
    date_hierarchy = 'dob'

admin.site.register(Volunteer, VolunteerAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Appointment, AppointmentAdmin)


class AuditLogAdmin(admin.ModelAdmin):
    pass

admin.site.register(AuditLog, AuditLogAdmin)


class StatusAdmin(admin.ModelAdmin):
    pass

admin.site.register(Status, StatusAdmin)
