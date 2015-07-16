from django.contrib import admin
from .models import FamHistQuestionnaire


class FamHistQuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('user', 'finished')

admin.site.register(FamHistQuestionnaire, FamHistQuestionnaireAdmin)
