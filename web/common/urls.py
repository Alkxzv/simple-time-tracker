from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

accounts = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
]

urlpatterns = [
    url(r'^accounts/', include(accounts, namespace='accounts')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
]
