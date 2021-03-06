from django.conf import settings
from django.conf.urls import patterns, include, url
import page
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^django_test/', include('django_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('home.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^login/', 'page.views.register'),
    url(r'^events/', include('events.urls')),
	url(r'^profile/', include('user_profile.urls')),
    url(r'^rush/', include('rush.urls')),
    url(r'^resources/', include('resources.urls')),
    url(r'^house-info/', include('house_info.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
		'document_root': settings.MEDIA_ROOT,
	}), )
else:
	urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', 'page.views.serve_media'), )

handler404 = 'page.views.custom_404'
