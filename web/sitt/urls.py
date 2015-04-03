from django.conf.urls import include, url


urlpatterns = [
    url(r'^', include('common.urls')),
    url(r'^', include('tracker.urls', namespace='tracker')),
]
