from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index),
    url(r'new', views.open_new),
    url(r'^blogs/(?P<num>\d+)$', views.showNumber),
    url(r'^blogs/(?P<num>\d+)/edit$', views.edit),
    url(r'^blogs/(?P<num>\d+)/delete$', views.destroy),
]