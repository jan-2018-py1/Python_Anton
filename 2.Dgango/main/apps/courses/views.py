# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import Comment, Course 
from django.contrib import messages

# Create your views here.
def index(request):
    cource_list = Course.objects.all()
    context = {
        'courses': cource_list,
    }
    return render(request, "courses/index.html", context)

def add_course(request):
    errors = Course.objects.validator(request.POST)
    if(len(errors)):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/courses')
    else:
        Course.objects.create(name = request.POST['name'],  description= request.POST['desc'])
    return redirect('/courses')

def comments(request, course_id):
    all_comments = Comment.objects.filter(course = Course.objects.get(id=course_id))
    context = {
        'comments':all_comments,
        'course_id':course_id
    }
    return render(request, "courses/comments.html", context)

def add_comment(request, course_id):
    Comment.objects.create(comment = request.POST['comment'],  course=Course.objects.get(id=course_id))
    link = "/courses/comments/" + str(course_id)
    return redirect(link)

def delete(request, id):
    course_info = Course.objects.get(id = id)
    context = {
        'course':course_info
    }
    return render(request, "courses/delete.html", context)

def destroy(request, id):
    this_course = Course.objects.get(id=id)
    this_course.delete()
    return redirect("/courses")