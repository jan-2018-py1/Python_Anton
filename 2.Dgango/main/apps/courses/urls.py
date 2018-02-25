from django.conf.urls import url
from . import views  

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add/$', views.add_course),
    url(r'^comments/(?P<course_id>\d+)$', views.comments),
    url(r'^add_comment/(?P<course_id>\d+)$', views.add_comment),
    url(r'^destroy/(?P<id>\d+)$', views.delete),
    url(r'^destroy/(?P<id>\d+)/confirmed$', views.destroy),
]