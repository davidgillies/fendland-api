from django.contrib import admin
from questionnaire.models import Users, Results, Progress, Questionnaires, Roles, Groups


class UsersAdmin(admin.ModelAdmin):
    search_fields = ('user_id',)

admin.site.register(Users, UsersAdmin)


class ResultsAdmin(admin.ModelAdmin):
    search_fields = ('user__user_id', 'questionnaire_id')
    list_display = ('user', 'questionnaire_id', 'var_id', 'var_name', 'var_value')
    list_filter = ('questionnaire_id',)

admin.site.register(Results, ResultsAdmin)


class ProgressAdmin(admin.ModelAdmin):
    list_filter = ('questionnaire_id', 'started', 'finished')
    search_fields = ('user__user_id', 'questionnaire_id')
    list_display = ('user', 'questionnaire_id', 'started', 'finished')

admin.site.register(Progress, ProgressAdmin)


class QuestionnairesAdmin(admin.ModelAdmin):
    list_filter = ('study_name', 'questionnaire_id')
    list_display = ('questionnaire_id', 'questionnaire_name', 'study_name')

admin.site.register(Questionnaires, QuestionnairesAdmin)


class RolesAdmin(admin.ModelAdmin):
    search_fields = ('user__user_id',)
    list_display = ('user_id', 'role')
    list_filter = ('role',)

admin.site.register(Roles, RolesAdmin)


class GroupsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'study_name', 'user_group')
    list_filter = ('study_name', 'user_group')

admin.site.register(Groups, GroupsAdmin)
