from django.conf.urls import patterns, include, url
import page
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^django_test/', include('django_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	#url('', 'page.views.welcome'),
    #url(r'^home/', 'page.views.home'),
    url(r'^$', 'page.views.home'),
    url(r'^home/', include('home.urls')),
    #url(r'^login/', 'page.views.register'),
    url(r'^login/', 'page.views.register'),
    url(r'^events/', include('events.urls')),
    #url(r'^events/', 'page.views.events'),
    url(r'^rush/', include('rush.urls')),
    url(r'^resources/', include('resources.urls')),
    #url(r'^rush/', 'page.views.rush'),
    url(r'^house-info/', 'page.views.house'),
)

handler404 = 'page.views.custom_404'
