from django.conf.urls import url, include

from . import views


events = [
    url(r'^$', views.EventListView.as_view(), name='index'),
    url(r'^create/$', views.EventCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.EventView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$',
        views.EventUpdateView.as_view(),
        name='update'),
]

entries = [
    url(r'^$', views.EntryListView.as_view(), name='index'),
    url(r'^create/$', views.EntryCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.EntryView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/close/$', views.EntryCloseView.as_view(), name='close'),
    url(r'^(?P<pk>\d+)/update/$',
        views.EntryUpdateView.as_view(),
        name='update'),
]

tags = [
    url(r'^$', views.TagListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.TagView.as_view(), name='detail'),
]

urlpatterns = [
    url(r'^events/', include(events, namespace='events')),
    url(r'^entries/', include(entries, namespace='entries')),
    url(r'^tags/', include(tags, namespace='tags')),
    url(r'^stats/$', views.StatsView.as_view(), name='stats'),
    url(r'^top/$', views.TopView.as_view(), name='top'),
    url(r'^$', views.MainView.as_view(), name='main'),
]
