from django.conf.urls import include, url
from django.contrib import admin


accounts = [
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        {'next_page': '/'},
        name='logout'),
]

urlpatterns = [
    url(r'^accounts/', include(accounts, namespace='accounts')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
]
