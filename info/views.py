from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    return render(request, 'info/about.html')

def info(request):
    return render(request, 'info/Info.html')

def learn_more(request):
    return render(request, 'info/learn_more.html')