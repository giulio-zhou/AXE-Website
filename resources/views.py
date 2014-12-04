# Create your views here.
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from page.models import LoginForm, RegisterForm, RegCode, Member
import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(__file__)) + '/resources/templates'

def resources(request):
    if request.method == 'POST':
        if 'logout' in request.POST:
            logout(request)
    return render(request, BASE_DIR + '/resources.html', {'is_logged_in': request.user.is_authenticated(), 'user_name': request.user})

def test_bank(request):
    if request.method == 'POST':
        if 'logout' in request.POST:
            logout(request)
    if not request.user.is_authenticated():
        return redirect('/login')
    from resources.models import Exam
    exams = Exam.objects.all()
    return render(request, BASE_DIR + '/exams.html', {'is_logged_in': request.user.is_authenticated(), 
                    'user_name': request.user, 'MEDIA_ROOT': settings.MEDIA_ROOT, 'BASE_URL': baseurl(request), 'exams': exams})

def baseurl(request):
    if request.is_secure():
        scheme = 'https://'
    else:
        scheme = 'http://'
    return scheme + request.get_host()
