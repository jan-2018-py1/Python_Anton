# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(req):
    return render(req, "login/login.html")

def createuser(request):
    errors = User.objects.validator(request.POST)
    if(len(errors)):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/login')
    else:
        hashed_pass = User.objects.hash_it(request.POST['pass'])
        User.objects.create(first_name = request.POST['f_name'],  last_name = request.POST['l_name'], email = request.POST['email'], password = hashed_pass)
        messages.success(request, 'The user is created!')
    return redirect("/login")

def login(request):
    errors = User.objects.login(request.POST)
    if(len(errors)):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/login')
    else:
        if 'name' not in request.session:
            request.session['name'] =  User.objects.get(email=request.POST['login_email']).first_name
    return redirect("/login/success/")


def success(req):
    context = {
        'first_name': req.session['name']
    }
    return render(req, "login/success.html", context)

def signout(req):
    req.session.flush()
    return redirect("/login")