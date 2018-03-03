from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index),
    url(r'registration/$', views.user_registration),
    url(r'login', views.login),
    url(r'book/$', views.books),
    url(r'add', views.add),
    url(r'reset', views.signout),
    url(r'^create/$', views.addbook),
    url(r'^users/(?P<id>\d+)$', views.user, name="show_user"),
    url(r'^book/(?P<id>\d+)$', views.book_info, name="show_book"),
    url(r'^review_it/(?P<id>\d+)$', views.reviewit),
   
    
    

]