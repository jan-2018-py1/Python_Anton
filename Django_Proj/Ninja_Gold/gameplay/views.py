# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import datetime
import random
# Create your views here.

log = 'the game is started! ' + str(datetime.datetime.now()) + '\n'

def index(request):
    if 'logs' not in request.session:
        request.session['logs'] =  [log]
        request.session['golds'] = 0
    context = {
        'logs' : request.session['logs'],
        'gold' : request.session['golds']
    }
    return render(request, 'ninja/index.html', context)

def process_money(request, place):
    request.session['loc'] = place
    if place == 'farm':
        money = makeGold(10, 21)
        message = "Earned " + str(money)+ " gold from the farm! " + str(datetime.datetime.now()) + '\n'
        request.session['golds']+=money
        request.session['logs'].append(message)
    if place == 'cave':
        money = makeGold(5, 11)
        message = "Earned " + str(money)+ " gold from the cave! " + str(datetime.datetime.now()) + '\n'
        request.session['golds']+=money
        request.session['logs'].append(message)
    if place == 'house':
        money = makeGold(2, 6)
        message = "Earned " + str(money)+ " gold from the house! " + str(datetime.datetime.now()) + '\n'
        request.session['golds']+=money
        request.session['logs'].append(message)
    if place == 'casino':
        if random.randrange(2) == 1:
            money = makeGold(0, 51)
            message = "Earned " + str(money)+ " gold from the casino! " + str(datetime.datetime.now()) + '\n'
            request.session['golds']+=money
            request.session['logs'].append(message)  
        else:
            money = makeGold(0, 51)
            message = "Entered a casino and lost " + str(money)+ "  gold... Ouch " + str(datetime.datetime.now()) + '\n'
            request.session['golds']-=money
            request.session['logs'].append(message)  
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')

def makeGold(min, max):
    result = random.randrange(min,max)
    return result