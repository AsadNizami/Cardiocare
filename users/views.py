from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from app import utility as util
from .models import User
from django.contrib.auth import login as auth_login


def login(request):
    if request.user.is_authenticated:
        print(request.user.is_authenticated)
        messages.info(request, f'Logout from the current account first')
        return redirect('landing')

    if request.method == 'POST':

        # username = request.POST['username']
        # password = request.POST['password']
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('landing')

        else:
            messages.warning(request, 'Invalid Credentials')
            return redirect('login')
        # user = auth.authenticate(username=username, password=password)
        #
        # if user:
        #     return redirect('landing')
        #
        # else:
        #     messages.error(request, f'No account found for {username}')
        #     return redirect('login')
    else:
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})


def register(request):
    if request.user.is_authenticated:
        messages.info(request, f'Logout from the current account first')
        return redirect('landing')

    elif request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data.get('email'))
            messages.success(request, f'Account created ! ')
            util.join_mail(form.cleaned_data.get('email'))
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', context={'form': form})


@login_required()
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


def delete_user(request):
    print(request.user.pk)
    User.objects.get(pk=request.user.pk).delete()
    messages.success(request, f'Your account has been deleted!')

    return redirect('landing')
