from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("اولین صفحه‌ی من")
