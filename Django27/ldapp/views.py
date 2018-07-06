# -*- coding: utf-8 -*-
from django.shortcuts import render
from  django.http import HttpResponse
import requesthander



def index(request):
    return  render(request,'ldapp/index.html')

def appuploadpic(request):
    print "收到App上传照片的请求"
    requesthander.handuploadimage(request)
    data = {
            'msg': '传照片成功_success'
        }
    return requesthander.handdictojson(data)

def applogin(request):
    print  '收到App登录请求'
    cusObj = request.POST["sign"]
    cusObjDic = requesthander.handjsontodict(cusObj)
    count = cusObjDic['parameters']['count']
    password = cusObjDic['parameters']['password']
    if count == 'zengjiangjun' and password == '168':
        data = {
            'msg': '登录成功_success'
        }
        return requesthander.handdictojson(data)
    else:
        print '登录失败'
        return ''
    

def appget(request):
    print  '收到App的Get请求'
    cusObj = request.GET["sign"]
    cusObjDic = requesthander.handjsontodict(cusObj)
    print(cusObjDic['lingda'])
    data = {
            'msg': 'Get成功_success'
        }
    return requesthander.handdictojson(data)


def webuploadpic(request):
    print "收到web传来的数据"
    requesthander.handuploadimage(request)
    data = {
            'msg': '上传照片成功_success'
        }
    return requesthander.handdictojson(data)


def webpost(request):
    print '收到web的post请求'
    cusObj = request.POST['sign']
    print (cusObj)
    data = {
            'msg': 'post请求成功_success'
        }
    return requesthander.handdictojson(data)

def webget(request):
    print '收到web的get请求'
    cusObj = request.GET['sign']
    print (cusObj)
    data = {
            'msg': 'get请求成功_success'
        }
    return requesthander.handdictojson(data)


def testtitle(request):
    print  '收到测试url'
    title = request.GET["title"]
    data = {
        'title':title
    }
    return  requesthander.handdictojson(data)

def test(request):
    print  '收到测试url'
    data = {
        'name':'我是三目童子',
        'address':'太阳上面',
        'money':'100000000'
    }
    return  requesthander.handdictojson(data)
