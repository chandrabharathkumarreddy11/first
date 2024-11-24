from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def india(request):
    return HttpResponse('I love my india')

def charan(request):
    return HttpResponse('<h1> Hi i am Ram charan</h1>')

def river(request):
    return HttpResponse('<h3>Narmada is holy river<h3>')