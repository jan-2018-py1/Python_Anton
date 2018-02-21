# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, "blog_app/index.html")

def open_new(request):
    response = 'placeholder to display a new form to create a new blog'
    return HttpResponse(response)

def showNumber(request, num):
    response = 'placeholder to display blog ' + num
    return HttpResponse(response)

def edit(request, num):
    response = 'placeholder to edit blog ' + num
    return HttpResponse(response)

def destroy(request, num):
    return redirect('/')