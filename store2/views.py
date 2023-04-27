from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>Hello</h2>')

def goodbye(request):
    return HttpResponse('<h1>Good Bye</h2>')
def welcome(request):
    return HttpResponse('<h1>welcome</h2>')


def thankyou(request):
    return HttpResponse('<h1>thankyou</h2>')

# Create your views here.
