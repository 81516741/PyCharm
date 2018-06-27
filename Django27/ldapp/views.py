# -*- coding: utf-8 -*-
from django.shortcuts import render
from  django.http import HttpResponse
import json
import requesthander



def index(request):
    return  render(request,'ldapp/index.html')


def handlepic(request):
    print "收到网页传来的数据"
    value = requesthander.handuploadimage(request)
    return HttpResponse(value)

def uploadpic(request):
    print "收到App传来的数据"
    requesthander.handuploadimage(request)
    data = {
        'code': "成功",
        'name': '小麻子',
        'age': '88'
    }
    json_str = json.dumps(data)
    return HttpResponse(json_str)
