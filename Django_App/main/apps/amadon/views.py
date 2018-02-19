# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

store = {
        0:["Tshirt", 19.99],
        1:["Sweater", 29.99],
        2:["Cup", 9.50],
        3:["Book", 49.99],
        4:["Logo", 1.00]
    }

def index(request):
    context = {
        'storedata' : store
    }
    if 'cart' not in request.session:
        request.session['cart'] = 0
    return render(request, 'amadon/index.html', context)

def checkout(request):
    product_index = str(unicode(request.POST['product_id']))
    quantity = str(unicode(request.POST['quantity']))
    total = store[int(product_index)][1]
    charge = float(quantity) * total
    request.session['cart'] += charge
    context = {
        'price' : charge,
        'number_items' : quantity
    }
    return render(request, 'amadon/checkout.html', context)

def reset(request):
    request.session.flush()
    return redirect('/amadon')