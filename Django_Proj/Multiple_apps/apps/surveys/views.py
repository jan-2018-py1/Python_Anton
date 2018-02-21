# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    response = 'placeholder to display all the surveys created'
    return HttpResponse(response)

def open_new(request):
    response = 'placeholder for users to add a new survey'
    return HttpResponse(response)