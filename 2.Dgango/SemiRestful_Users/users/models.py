# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}

        if(len(postData['f_name'])) < 1:
            errors['first_name'] = "The first name cannot be blank"
        
        if(len(postData['l_name'])) < 1:
            errors['last_name'] = "The last name cannot be blank"
        
        if len(postData['email']) < 1:
            errors['email'] = "Email cannot be blank!"
        
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid Email!"
        
        return errors


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = UserManager()