# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Messages(models.Model):
    msg_no = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=15)
    content = models.CharField(max_length=100)
    author = models.CharField(max_length=10)
    user_id = models.CharField(max_length=30)
