# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
from django.core.exceptions import ObjectDoesNotExist

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Validator(models.Manager):
    def validator(self, postData):
        errors = {}
        try: 
            if User.objects.get(email=postData['email']):
                errors['not_unique'] = 'The email exists in DB!'
        except:
            pass
        if(len(postData['name'])) < 1:
            errors['name'] = "Invalid Name!"
        if(len(postData['alias'])) < 1:
            errors['alias'] = "Invalid alias!"    
        if(len(postData['pass'])) < 8:
            errors['pass'] = "Invalid Password! The minimum length is 8 characters"
        if postData['pass'] != postData['cpass']:
            errors['pass'] = "The password should match!"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid Email format!"         
        return errors

    def hash_it(self, pwd):
        password = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())
        return password

    def login(self, postData):
        errors = {}
        if(len(postData['lemail'])) < 1:
            errors['lemail'] = "Invalid Email!"
            return errors
        if(len(postData['lpass'])) < 1:
            errors['lname'] = "Invalid Password!"
            return errors
        try: 
            find_user = User.objects.get(email = postData['lemail'])
            if not bcrypt.checkpw(postData['lpass'].encode(), find_user.password.encode()):
                errors['login_fail'] = "The password doesn't match!"
            return errors
        except ObjectDoesNotExist:
            errors['nouser'] = "The user doesn't exist!"
        return errors

class BookValidation(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if(len(postData['title'])) < 1:
            errors['title'] = "The title cannot be blank!" 
        if(len(postData['review'])) < 1:
            errors['pass'] = "The review cannot be blank!"
        if ('author' not in postData) and (len(postData['newauthor'])) < 1:
            errors['pass'] = "The author field cannot be blank!"         
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=55)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = Validator()

class Author(models.Model):
    author = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    objects = BookValidation()
    
class Comment(models.Model):
    text = models.TextField()
    book = models.ForeignKey(Book, related_name="comments")
    user = models.ForeignKey(User, related_name="comments")
    created_at = models.DateTimeField(auto_now_add = True)