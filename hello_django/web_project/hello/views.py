# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, Django!")
def brian(request):
    return HttpResponse("hello, brian")
def david(request):
    return HttpResponse("hello, david bo!")

def greet(request, name):
    return HttpResponse(f"hello, {name.capitalize()}!")