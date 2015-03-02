from django.conf.urls import patterns, include, url
from django.contrib import admin
from html_renderer import views as html_renderer_views
from api_renderer import views as api_renderer_views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^html/(\w+)/(\w+)/(\w+)', csrf_exempt(html_renderer_views.HTMLView.as_view())),
    url(r'^html/(\w+)/(\w+)', csrf_exempt(html_renderer_views.HTMLView.as_view())),
    url(r'^html/(\w+)', csrf_exempt(html_renderer_views.HTMLView.as_view())),
    urlr'^html/', csrf_exempt(html_renderer_views.HTMLView.as_view())),
    url(r'^api/(\w+)/(\w+)/(\w+)', csrf_exempt(api_renderer_views.APIView.as_view())),
    url(r'^api/(\w+)/(\w+))', csrf_exempt(api_renderer_views.APIView.as_view())),
    url(r'^api/(\w+)', csrf_exempt(api_renderer_views.APIView.as_view())),
    url(r'^api/', csrf_exempt(api_renderer_views.APIView.as_view())),
)
