from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	pledge_year = models.IntegerField()
	fall_pledge = models.BooleanField(default=False)
	year_in_school = models.IntegerField()
	major = models.CharField(max_length=100, blank=True)
	def __unicode__(self):
		return self.user.username 
