from django.conf.urls import patterns, include, url
from django.contrib import admin
from html_renderer import views as html_renderer_views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^a/', csrf_exempt(html_renderer_views.HTMLView.as_view()) ),
#   url(r'^b/', 'api_renderer.views.tester'),
)
