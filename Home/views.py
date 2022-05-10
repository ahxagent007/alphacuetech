from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

# Create your views here.

def Home(request):
    return HttpResponse("HELLO")
