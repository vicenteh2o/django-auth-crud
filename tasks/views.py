from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse("User created successfully")
            except:
                return HttpResponse("Username already exists")
        return HttpResponse("Passwords dont match")
    else:
        print("Received GET request for signup")
        return render(request, 'signup.html', {'form': UserCreationForm()})
