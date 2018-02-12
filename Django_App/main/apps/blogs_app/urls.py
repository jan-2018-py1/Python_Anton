from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'new', views.new),
    url(r'create', views.create),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^(?P<number>\d+)/edit$', views.edit),
    url(r'^(?P<number>\d+)/destroy$', views.destroy)
]

"""
'^' Matches the following characters at the beginning of a string. Example: '^a' matches 'anna' but not 'banana'.
'$' Matches the previous characters at the end of a string. Example: 'a$' matches 'anna' and 'banana' but not 'fan'.
'[]' Matches any value in a range. Example: '[0-9]' matches '9' and '9s'.
'{n}' Matches n number or more repetitions of the preceding pattern. Example: '[0-9]{2}' matches '91' and '9834' but not '9'
\d Matches digits.  Example: "\d" matches "8" and "877x"
\d+ matches a string with one or more digits
\w Matches characters.
\w+ matches a string with one or more character/word

url(r'^articles/(?P\d+)$', views.show)
url(r'^articles/(?P\w+)$', views.show_word)
url(r'^articles/2003/$', views.special_case_2003)
url(r'^articles/(?P[0-9]{4})$', views.year_archive)
url(r'^articles/(?P[0-9]{4})/(?P[0-9]{2}$', views.month_archive)
"""