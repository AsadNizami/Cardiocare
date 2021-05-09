from django.shortcuts import render
from django.http import HttpResponse
from .forms import InviteForm
from .utility import invite_mail
from django.contrib import messages


def about(request):
    if request.method == 'POST':
        email = request.POST['email']
        invite_mail(request, email)
        messages.success(request, f'Invitation sent!')
        print(email)

    form = InviteForm()
    context = {'form': form}
    return render(request, 'info/about.html', context)

def info(request):
    return render(request, 'info/Info.html')

def learn_more(request):
    return render(request, 'info/learn_more.html')
