from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	likes = models.IntegerField()

	def __unicode__(self):
		return self.title	

class Member(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    pledge_year = models.IntegerField()
    fall_pledge = models.BooleanField(default=False)
    year_in_school = models.IntegerField()
    major = models.CharField(max_length=100, blank=True)
    def __unicode__(self):
        return self.user.username

class LoginForm(forms.Form):
	your_name = forms.CharField(label='Your Name', max_length=100)
	password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput())

class RegisterForm(forms.Form):
	first_name = forms.CharField(label='First Name', max_length=100)
	last_name = forms.CharField(label='Last Name', max_length=100)
	your_name = forms.CharField(label='Username', max_length=100)
	password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput())
	#password_confirm = forms.CharField(label='Confirm Password', max_length=50, widget=forms.PasswordInput())
	email = forms.CharField(label='Email', max_length=100)
	regcode = forms.CharField(label='Registration Code', max_length=100)
	pledge_year = forms.IntegerField()
	major = forms.CharField(label='Major', max_length=100)

class RegCode(models.Model):
    code = models.CharField(max_length = 200)
    def __unicode__(self):
        return self.code
