from django.conf.urls import url
from . import views  

urlpatterns = [
    url(r'^$', views.index),
    url(r'new/$', views.addNew),
    url(r'^(?P<id>\d+)/edit$', views.edit),
    url(r'^(?P<id>\d+)/updateuser$', views.edit_user),
    url(r'^(?P<id>\d+)/destroy$', views.delete_user),
    url(r'^user/(?P<id>\d+)$', views.show),
    url(r'^new/create/$', views.create),
    
    

   #url(r'^process_money/(?P<place>\w+)$', views.process_money),
   # url(r'reset', views.reset)
]