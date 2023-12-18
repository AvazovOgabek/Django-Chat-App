from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Profile
from django.contrib.auth.decorators import login_required



def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email_input = request.POST.get('gmail')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(email=email_input).exists():
                messages.error(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email_input, password=password, first_name=first_name, last_name=last_name)

                new_profile = Profile.objects.create(user=user, last_name=last_name, first_name=first_name)

                new_profile.save()
                auth.login(request, user)
                return redirect('signin')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
    else:
        return render(request, 'registrations/signup.html')

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user) 
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('signin')
    else:
        return render(request, 'registrations/signin.html')