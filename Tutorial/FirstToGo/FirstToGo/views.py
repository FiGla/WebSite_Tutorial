from django.http import HttpResponse
from django.shortcuts import render

def about (request):

    return render(request,"about.html",{})

def posts_home (request,num):
    return HttpResponse("<h1>Hello </h1>")
