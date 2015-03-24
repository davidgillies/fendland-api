from django.contrib import admin
from questionnaire.models import Users, Results, Progress, Questionnaires, Roles, Groups


class UsersAdmin(admin.ModelAdmin):
    pass

admin.site.register(Users, UsersAdmin)


class ResultsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Results, ResultsAdmin)


class ProgressAdmin(admin.ModelAdmin):
    pass

admin.site.register(Progress, ProgressAdmin)


class QuestionnairesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Questionnaires, QuestionnairesAdmin)


class RolesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Roles, RolesAdmin)


class GroupsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Groups, GroupsAdmin)
