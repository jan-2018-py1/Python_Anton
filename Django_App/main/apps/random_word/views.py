# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request, methods = "GET"):
  if "attempts" not in request.session:
    request.session["attempts"] = 0
    request.session["code"] = "--------------"
  return render(request,'random_code/index.html')

def getCode(request):
  request.session["code"] = get_random_string(length=14)
  request.session["attempts"] +=1
  return redirect('/code')