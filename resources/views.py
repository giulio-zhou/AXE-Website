# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from page.models import LoginForm, RegisterForm, RegCode, Member
import sys                                                                                                                                 

def resources(request):
    return render(request, 'resources.html')
