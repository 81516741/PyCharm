from django.conf.urls import url
from  . import views
urlpatterns = [
    url('^$', views.index),
    url('^appuploadpic', views.appuploadpic),
    url('^applogin', views.applogin),
    url('^appget', views.appget),
    url('^webuploadpic', views.webuploadpic),
    url('^webpost', views.webpost),
    url('^webget', views.webget),
    url('^testtitle', views.testtitle),
    url('^test', views.test),
]