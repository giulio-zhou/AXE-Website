# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from page.models import LoginForm, RegisterForm, RegCode, Member
import sys

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

def login2(request):
	username = 'gzhou'
	password = 'GiUlIo76'
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponse("<html><body>Logged in and active!</body></html>")
		else:
			return HttpResponse("<html><body>Logged in but you're inactive!</body></html>")
	return HttpResponse("<html><body>Authentication failed!</body></html>")
					
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

'''def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			try:
				if form.cleaned_data['password'] == form.cleaned_data['password_confirm']:
					regcode = RegCode.objects.get(code=form.cleaned_data['regcode'])
					regcode.delete()
					user = User.objects.create_user(form.cleaned_data['your_name'], form.cleaned_data['email'], form.cleaned_data['password'])
					return HttpResponse("<html><body>Successfully Registered User %s!</body></html>" % form.cleaned_data['your_name'])
			#return HttpResponse("<html><body>lolol</body></html>")
			except RegCode.DoesNotExist:
				print 'lol'
				return HttpResponse("<html><body>Wrong reg code</body></html>")
		#form = RegisterForm()
		return HttpResponse("<html><body>{0}  {1}  {2}</body></html>".format(form.cleaned_data, form.is_valid, RegCode.objects.all()))
	else:
		form = RegisterForm()
	return render(request, 'index.html', {'form' : form})
'''

def register(request):
	if request.method == 'POST':
		#return HttpResponse('<html><body>{0}  {1}</body></html>'.format(request.POST, RegCode.objects.all()))
		#print request.POST, 'submit1' in request.POST
		if 'submit2' in request.POST:
			form = RegisterForm(request.POST)
			print request.method, form.is_valid(), request.POST
			if form.is_valid():
				try:
				#   if form.cleaned_data['password'] == form.cleaned_data['password_confirm
						regcode = RegCode.objects.get(code=form.cleaned_data['regcode'])
						regcode.delete()
						user = User.objects.create_user(form.cleaned_data['your_name'],
									form.cleaned_data['email'] + '@berkeley.edu', form.cleaned_data['password'])
						user.member = Member(pledge_year=form.cleaned_data['pledge_year'], fall_pledge=True,
							                                                    year_in_school=2, major=form.cleaned_data['major'])
						user.first_name = form.cleaned_data['first_name']
						user.last_name = form.cleaned_data['last_name']
						#print user.member
						user.save()
						user.member.save()
						return HttpResponse("<html><body>Successfully Registered User %s!</body></html>" % form.cleaned_data['your_name'])
				#return HttpResponse("<html><body>lolol</body></html>")
				except RegCode.DoesNotExist:
					print 'lol'
			form = RegisterForm()
		elif 'submit1' in request.POST:
			form = LoginForm(request.POST)
			#print 'Trying to log in'
			if form.is_valid():
				user = authenticate(username=form.cleaned_data['your_name'], password=form.cleaned_data['password'])
				#print user
				if user is not None:
					login(request, user)
#return HttpResponse('Successfully logged in user %s!' % user.username)
			form = RegisterForm()
		elif 'submit3' in request.POST:
			logout(request)
			form = RegisterForm()
		#return HttpResponse("<html><body>%s</body></html>" % request.POST.__str__())
	else:
		#fsock.write(request.GET)
		form = RegisterForm()
		#return HttpResponse("<html><body>{0}  {1}</body></html>".format(request.POST, RegCode.objects.all()))
	return render(request, 'login_page.html', {'form' : form, 'is_logged_in' : request.user.is_authenticated(), 'user_name': request.user})

def home(request):
    return render(request, 'home.html')

def events(request):
    return render(request, 'events.html')

def rush(request):
    return render(request, 'rush.html')

def house(request):
    return render(request, 'house.html')
