from django.conf.urls import  url
from django.conf.urls.static import static
from django.contrib import admin

from . import views

urlpatterns = [

    url(r'^crea/$',"FirstToGo.views.posts_home"),
    url(r'^abc/$',"FirstToGo.views.posts_home"),
    url(r'^abc/$',"FirstToGo.views.posts_home"),
    url(r'^abc/$',"FirstToGo.views.posts_home"),
]
