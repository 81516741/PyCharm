# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms

class PeopleInfo(models.Model):
    pname = models.CharField(max_length=20,default='')
    paddress = models.CharField(max_length=20,default='')
    def __str__(self):
        return self.pname.encode('utf-8') + '好样的' +self.paddress.encode('utf-8')

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20,default='')
    bprice = models.CharField(max_length=10,default='')
    bauthor = models.CharField(max_length=10,default='')
    def __str__(self):
        return self.btitle.encode('utf-8')

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20,default='')
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=100,default='')
    hBook = models.ForeignKey('BookInfo')
    def __str__(self):
        return self.hname.encode('utf-8')


class BookInfoForm(forms.ModelForm):
    class Meta:
        # 指定 Model
        model = BookInfo
        # Form 需要 Model 中的哪几个 Field
        fields = ['btitle','bprice']
        # Form 排除 Model 中的哪几个 Field
        exclude = ['author']
