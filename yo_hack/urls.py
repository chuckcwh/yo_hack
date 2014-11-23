from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from yo_hack import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'yo_hack_app.views.index', name='index'),
    url(r'^dashboard/$', 'yo_hack_app.views.dashboard', name='dashboard'),
    url(r'^profile/$', 'yo_hack_app.views.profile', name='profile'),


    url(r'^admin/', include(admin.site.urls)),

    #ajax
    url(r'^hello/$', 'yo_hack_app.views.hello', name='hello'),
    url(r'^emergency/$', 'yo_hack_app.views.emergency', name='emergency'),
    url(r'^im-lost/$', 'yo_hack_app.views.im_lost', name='im_lost'),

    #rendering URL
    url(r'^emergency/(?P<emergency_id>[0-9]+)/$', 'yo_hack_app.views.emergency_url', name='emergency_url'),
    url(r'^lost/(?P<lost_id>[0-9]+)/$', 'yo_hack_app.views.lost_url', name='lost_url'),
    url(r'^hello/(?P<hello_id>[0-9]+)/$', 'yo_hack_app.views.hello_url', name='hello_url'),

    url(r'^action/$', 'yo_hack_app.views.action', name='action'),
    #User account
    url(r'^register/$', 'yo_hack_app.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)