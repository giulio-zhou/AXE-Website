from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from page.models import LoginForm, RegisterForm, RegCode, Member
import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(__file__)) + '/user_profile/templates/'

# Create your views here.

def user_profile(request):
	if request.method == 'POST':
		if 'logout' in request.POST:
			logout(request)
	user = request.user
	if not user.is_authenticated():
		return redirect('/login')
	return render(request, BASE_DIR + 'profile.html', {'is_logged_in': user.is_authenticated,
														'user_name': request.user,
														'user_profile': user.member})	
