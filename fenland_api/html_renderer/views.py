from django.views.generic import View
from django.http import HttpResponse
from api_renderer.views import fenland_app


class HTMLView(View):
    def get(self, request):
        return HttpResponse(fenland_app.name)
