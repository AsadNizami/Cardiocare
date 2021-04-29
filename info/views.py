from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    return render(request, 'info/about.html')

def info(request):
    return render(request, 'info/info.html')
