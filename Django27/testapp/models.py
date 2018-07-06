# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Dog(models.Model):
    pname = models.CharField(max_length=20,default='')
    paddress = models.CharField(max_length=20,default='')
    def __str__(self):
        return self.pname.encode('utf-8') + '好样的' +self.paddress.encode('utf-8')
