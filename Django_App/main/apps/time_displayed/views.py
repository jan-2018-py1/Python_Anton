# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime

def index(request):
  context = {
  "date": strftime("%b %d, %Y", gmtime()),
  "time": strftime("%I:%M %p", localtime())
  }
  return render(request,'time_displayed/index.html', context)