from django.db import models

# Create your models here.

class Exam(models.Model):
    instructor = models.CharField(max_length=100)
    key = models.BooleanField(default=False)
    term = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    year = models.IntegerField()
    pdf_path = models.CharField(max_length=100)
    exam = models.CharField(max_length=50)
    approved = models.BooleanField(default=False)
    def __unicode__(self):
        return self.pdf_path

