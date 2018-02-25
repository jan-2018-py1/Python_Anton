# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Validator(models.Manager):
    def validator(self, postData):
        errors = {}
        if(len(postData['name'])) < 1:
            errors['name'] = "The course name should be more than 5 characters"
        if(len(postData['desc'])) < 1:
            errors['desc'] = "The course description should be more than 15 characters"     
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = Validator()

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name="comments")
    created_at = models.DateTimeField(auto_now_add = True)
