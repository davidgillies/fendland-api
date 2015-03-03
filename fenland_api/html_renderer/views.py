from django.views.generic import View
from django.http import HttpResponse
from api_renderer.views import fenland_app
from django.shortcuts import render


class HTMLView(View):
    def get(self, request, section=None, id_variable=None,
            id_variable_value=None):
        # test using this data in a template
        section = fenland_app.get_section(1)
        result = {'section': section}
        return render(request, 'html_renderer/base.html', result)