from rest_framework.decorators import api_view
from django.shortcuts import HttpResponse
from rest_framework import status
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from .models import Query
import json
import datetime

#class CreateUser(requests):
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .forms import SignupForm
from django.contrib.auth.models import User



# Register new user
def register_new_user(request, success_status):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            login(request, user)
            #return redirect('')
    
        #return render(request, 'registration/register.html', {'form': form})
        return HttpResponse(json.dumps({"detail": "Registered user successfully"}), status=success_status)
    else:
        return HttpResponse(json.dumps({"detail": "please use POST method to register"}), status=status.HTTP_501_NOT_IMPLEMENTED)





@api_view(['GET', 'POST'])
def register(request):
    if request.user.is_anonymous:
        return HttpResponse(json.dumps({"detail": "Not authorized"}), status=status.HTTP_401_UNAUTHORIZED)
    
    if request.method == "POST":
        return register_new_user(request, status.HTTP_201_CREATED)
        
    return HttpResponse(json.dumps({"detail": "Wrong method"}), status=status.HTTP_501_NOT_IMPLEMENTED)


