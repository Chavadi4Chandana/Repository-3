from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def chandu(request):
    return HttpResponse('hi hello how are you')
