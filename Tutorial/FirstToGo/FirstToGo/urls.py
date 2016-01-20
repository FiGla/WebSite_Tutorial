from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$','newsletter.views.contact', name='contact'),
    url(r'^about/$', 'FirstToGo.views.about', name='about'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^posts/(?P<num>[0-9]+)/$','FirstToGo.views.posts_home')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root = settings.MEDIA_ROOT)
