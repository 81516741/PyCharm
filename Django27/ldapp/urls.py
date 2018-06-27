from django.conf.urls import url
from  . import views
urlpatterns = [
    url('^$', views.index),
    url('^handlepic', views.handlepic),
    url('^uploadpic', views.uploadpic),
]