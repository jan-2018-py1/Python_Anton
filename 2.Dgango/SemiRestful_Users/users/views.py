# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages

# Create your views here.

def index(request):
    context ={
        'users': User.objects.all()
    }
    return render(request,'users/index.html', context)

def show(request, id):
    context ={
        'user': User.objects.get(id=id)
    }
    return render(request,'users/user.html', context)

def addNew(request):
    return render(request,'users/new.html')

def edit(request, id):
    context = {
        'id': id
    }
    return render(request,'users/edit.html', context)

def edit_user(request, id):
    errors = User.objects.validator(request.POST)
    if(len(errors)):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            link = "/users/"+str(id)+"/edit"
        return redirect(link)
    else:
        user = User.objects.get(id=id)
        user.first_name = request.POST['f_name']
        user.last_name = request.POST['l_name']
        user.email_address = request.POST['email']
        user.save()
    return redirect("/users")

def create(request):
    errors = User.objects.validator(request.POST)
    if(len(errors)):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/new/')
    else:
        User.objects.create(first_name = request.POST['f_name'], last_name= request.POST['l_name'], email_address= request.POST['email'])
        new_user = User.objects.last()
        redirect_link = "/users/user/" +  str(new_user.id)
    return redirect(redirect_link)

def delete_user(request, id):
    this_user = User.objects.get(id=id)
    this_user.delete()
    return redirect("/users")
