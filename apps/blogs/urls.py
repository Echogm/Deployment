from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^blogs/new$', views.new),
    url(r'^blogs/create$', views.create),
    url(r'^blogs/(?P<postnumber>\d+)$', views.show),
    url(r'^blogs/(?P<postnumber>\d+)/edit$', views.edit),
    url(r'^blogs/(?P<postnumber>\d+)/delete$', views.destroy),
]
