# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from page.models import LoginForm, RegisterForm, RegCode, Member
import sys, os 
BASE_DIR = os.path.dirname(os.path.dirname(__file__)) + '/house_info/templates'

def house_info(request):
    return render(request, BASE_DIR + '/house.html', {'is_logged_in': request.user.is_authenticated(), 'user_name': request.user})
