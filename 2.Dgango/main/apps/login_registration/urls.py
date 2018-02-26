from django.conf.urls import url
from . import views  

urlpatterns = [
    url(r'^$', views.index),
    url(r'^success/$', views.success),
    url(r'^signout/$', views.signout),
    url(r'^reg/$', views.createuser),
    url(r'^sc/$', views.login)
]