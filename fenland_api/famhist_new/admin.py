from django.contrib import admin
from .models import FamHistQuestionnaire


class FamHistQuestionnaireAdmin(admin.ModelAdmin):
    pass

admin.site.register(FamHistQuestionnaire, FamHistQuestionnaireAdmin)
