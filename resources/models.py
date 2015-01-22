from django.db import models
from django import forms

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

EXAM_TYPE = (
    ('Midterm 1', 'Midterm 1'),
    ('Midterm 2', 'Midterm 2'),
    ('Midterm 3', 'Midterm 3'),
    ('Final', 'Final'),
)

TERM = (
    ('Fall', 'Fall'),
    ('Spring', 'Spring'),
)

class ExamForm(forms.Form):
    instructor = forms.CharField(max_length=100, label='Instructor')
    key = forms.BooleanField()
    term = forms.ChoiceField(choices=TERM, required=True, label='Term')
    subject = forms.CharField(max_length=50)
    course = forms.CharField(max_length=50)
    year = forms.IntegerField()
    exam = forms.ChoiceField(choices=EXAM_TYPE, required=True, label='Exam')
    test = forms.FileField()

def create_exam_path(data):
    exam_dict = {'Midterm 1': 'mt1', 'Midterm 2': 'mt2', 'Midterm 3': 'mt3', 'Final': 'final'}
    exam_type = 'exam' 
    if data['key']:
        exam_type = 'soln'
    contents = [data['subject'] + data['course'], data['term'] + str(data['year']), \
                exam_dict[data['exam']], data['instructor'], exam_type]
    return '-'.join(contents) + '.pdf'
