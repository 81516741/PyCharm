# -*- coding: utf-8 -*-
from django.conf import settings
import os

def handuploadimage(request):
    title = request.POST["sign"]
    print "sign%s" % title
    if request.FILES.has_key("avatar"):
        pic1 = request.FILES['avatar']
        picName = os.path.join(settings.MEDIA_ROOT, pic1.name)
        with open(picName, 'w') as pic:
            for c in pic1.chunks():
                pic.write(c)
        return '<img src="/static/media/%s"/>' % pic1.name

    return '没有传递参数'
