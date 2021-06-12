from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("<h1>Welcome...To Home Page of Django</h1>")

def aboutpage(request):
    return HttpResponse("<h1>Welcome...To About-Us Page of Django</h1>")

def contactpage(request):
    return HttpResponse("<h1>Welcome...To Contact Page of Django</h1>")
