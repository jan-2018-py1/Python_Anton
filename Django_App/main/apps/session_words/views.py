# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def index(request):
    if 'words' not in request.session:
        request.session['words'] =  []
    context = {
        'word_list' : request.session['words']
    }
    return render(request, "session/index.html", context)

def addWord(request):
    if request.POST.get('big', False) == "true":
        text = (request.POST['word']).upper()
    else: text = request.POST['word']
    words = { 'text': text, 'color': request.POST.get('color', 'none'), 'date':str(datetime.datetime.now()) }
    temp = request.session['words']
    temp.append(words)
    request.session['words'] = temp
    return redirect('/session')

def clear(request):
    request.session.flush()
    return redirect('/session')

# {u'color': u'Green', u'text': u'DDSF', u'date': u'2018-02-17 23:57:11.159000'}