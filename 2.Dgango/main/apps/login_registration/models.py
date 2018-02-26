# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
from django.core.exceptions import ObjectDoesNotExist


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class Validator(models.Manager):
    def validator(self, postData):
        errors = {}
        try: 
            if User.objects.get(email=postData['email']):
                errors['not_unique'] = 'The email exists in DB!'
        except:
            pass
        if(len(postData['f_name'])) < 1:
            errors['name'] = "Invalid First Name!"
        if(len(postData['l_name'])) < 1:
            errors['lname'] = "Invalid Last Name!"    
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
        if(len(postData['login_email'])) < 1:
            errors['name'] = "Invalid Email!"
            return errors
        if(len(postData['login_pass'])) < 1:
            errors['lname'] = "Invalid Password!"
            return errors
        try: 
            find_user = User.objects.get(email = postData['login_email'])
            if not bcrypt.checkpw(postData['login_pass'].encode(), find_user.password.encode()):
                errors['login_fail'] = "The password doesn't match!"
            return errors
        except ObjectDoesNotExist:
            errors['nouser'] = "The user doesn't exist!"
        return errors
    
    def user_name(self, postData):
        first_name = User.objects.get(email = postData['login_email'])
        return str(first_name)

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=55)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = Validator()


    