# Create your views here.
from django.conf import settings
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from page.models import LoginForm, RegisterForm, RegCode, Member
import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Create your views here.
def hello(request):
    name = "Giulio"
    html = "<html><body>Hi %s, this seems to have worked.</body></html>" % name
    return HttpResponse(html)

def chemistry(request):
    if (request.user.is_authenticated()):
        return HttpResponse("<html><body>Congrats, you're logged in!</body></html>")
    else:
        return redirect('/gzhou/django_test/hello')
def logout_view(request):
    logout(request)
    return HttpResponse("<html><body>Logged out!</body></html>")    

def reallogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['your_name'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)            
                    return HttpResponseRedirect('/chemistry')
                form = LoginForm()
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form' : form})

def register(request):
    if request.method == 'POST':
        if 'submit2' in request.POST:
            form = RegisterForm(request.POST)
            if form.is_valid():
                try:
                        regcode = RegCode.objects.get(code=form.cleaned_data['regcode'])
                        regcode.delete()
                        user = User.objects.create_user(form.cleaned_data['your_name'],
                                    form.cleaned_data['email'] + '@berkeley.edu', form.cleaned_data['password'])
                        member = Member(user=user, pledge_year=form.cleaned_data['pledge_year'], fall_pledge=True,
                                                                                year_in_school=2, major=form.cleaned_data['major'])
                        user.first_name = form.cleaned_data['first_name']
                        user.last_name = form.cleaned_data['last_name']
                        user.save()
                        member.save()
                        return HttpResponse("<html><body>Successfully Registered User %s!</body></html>" % form.cleaned_data['your_name'])
                except RegCode.DoesNotExist:
                    print 'Registration Code Does Not Exist'
            form = RegisterForm()
        elif 'submit1' in request.POST:
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(username=form.cleaned_data['your_name'], password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
            form = RegisterForm()
        elif 'logout' in request.POST:
            logout(request)
            form = RegisterForm()
    else:
        form = RegisterForm()
    return render(request, 'login_page.html', {'form' : form, 'is_logged_in' : request.user.is_authenticated(), 'user_name': request.user})

def home(request):
    return render(request, 'home.html')

def events(request):
    return render(request, 'events.html')

def rush(request):
    return render(request, 'rush.html')

def house(request):
    return render(request, 'house.html')

def custom_404(request):
    return render(request, '404.html', {'is_logged_in': request.user.is_authenticated(), 'user_name': request.user})

def serve_media(request, path):
    print settings.MEDIA_ROOT, path
    file_path = BASE_DIR + '/' + settings.MEDIA_ROOT + '/' + path
    with open(file_path, 'r') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'filename=' + path
        return response
    pdf.closed  
