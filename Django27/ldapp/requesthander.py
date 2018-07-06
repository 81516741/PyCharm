# -*- coding: utf-8 -*-
from django.conf import settings
from  django.http import HttpResponse
import os
import json

def handuploadimage(request):
    sign = request.POST["sign"]
    print "sign%s" % sign
    if request.FILES.has_key("avatar"):
        pic1 = request.FILES['avatar']
        picName = os.path.join(settings.MEDIA_ROOT, pic1.name)
        with open(picName, 'w') as pic:
            for c in pic1.chunks():
                pic.write(c)
        return '<img src="/static/media/%s"/>' % pic1.name

    return HttpResponse('没有传递参数')

def handdictojson(dic):
    return  HttpResponse(json.dumps(dic,ensure_ascii = False),content_type='application/json; charset=utf-8')

def handjsontodict(jsonstr):
    return  json.loads(jsonstr)