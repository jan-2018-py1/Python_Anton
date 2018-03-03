# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.

def checkSession(request):
    if 'name' not in request.session:
        return redirect ('/')

def index(request):
    if 'name' in request.session:
        return redirect ('/book')
    return render(request, 'belt/index.html')

def signout(req):
    req.session.flush()
    return redirect("/")

def user_registration(req):
    errors = User.objects.validator(req.POST)
    if(len(errors)):
        for tag, error in errors.iteritems():
            messages.error(req, error, extra_tags=tag)
        return redirect('/')
    else:
        hashed_pass = User.objects.hash_it(req.POST['pass'])
        User.objects.create(name = req.POST['name'],  alias = req.POST['alias'], email = req.POST['email'], password = hashed_pass)
        messages.success(req, 'The user is created!')
    return redirect("/")

def login(request):
    errors = User.objects.login(request.POST)
    if(len(errors)):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        if 'name' not in request.session:
            request.session['name'] =  User.objects.get(email=request.POST['lemail']).alias
            request.session['user_id'] = User.objects.get(email=request.POST['lemail']).id
    return redirect("/book")

def books(request):
    random_books = Book.objects.all().order_by('?')[:5]
    all_books = Book.objects.all().order_by('created_at').reverse()[:3]
    comments = Comment.objects.filter(book = all_books)

    context = {
        'books': all_books,
        'other_books': random_books,
        'comments': comments
    }
    return render(request, 'belt/books.html', context)

def addbook(request):
    checkSession(request) 
    errors = Book.objects.book_validator(request.POST)
    if(len(errors)):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/add')
    else:
        if (len(request.POST['newauthor'])) < 1:
            bookAuthor = Author.objects.get(author = request.POST['author'])
        else:
            bookAuthor = Author.objects.create(author = request.POST['newauthor'])
        user = User.objects.get(id = request.session['user_id'])
        bookTitle = str(request.POST['title'])
        Book.objects.create(title = bookTitle,  author = bookAuthor, rating = request.POST['rating'])
        Comment.objects.create(text = request.POST['review'], book = Book.objects.get(title = bookTitle), user=user)
    return redirect('/')

def add(request):
    authors = Author.objects.all()
    context ={
        'authors' : authors
    }
    return render(request, 'belt/add.html', context)
    
def user(request, id):
    this_user = User.objects.get(id=id)
    context = {
        "user": this_user,
        "total": Comment.objects.filter(user = this_user).count()
    }
    return render(request, 'belt/users.html', context)

def book_info(request, id):
    this_book = Book.objects.get(id=id)
    reviews = Comment.objects.filter(book = this_book)
    context = {
        "book": this_book,
        "reviews": reviews
    }
    return render(request, 'belt/book.html', context)

def reviewit(request, id):
    user = User.objects.get(id= request.session['user_id'])
    this_book = Book.objects.get(id = id)
    total_comments = Comment.objects.filter(book = this_book).count()
    rating = (int(this_book.rating) + int(request.POST['rating']))/(total_comments+1)
    this_book.rating = rating
    this_book.save()
    Comment.objects.create(text = request.POST['review'], book = this_book, user=user)
    return redirect('/book')