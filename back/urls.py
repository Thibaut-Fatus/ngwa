from django.conf import settings
from django.views.generic.base import RedirectView
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from views import angular_app


urlpatterns = patterns('',
    url(r'^home/$', angular_app, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', RedirectView.as_view(url='/index.html')),
    url(r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^login$', 'django.contrib.auth.views.login', {"authentication_form": AuthenticationForm}, name="login"),
    url(r'^', RedirectView.as_view(pattern_name='login', permanent=False)),
)
