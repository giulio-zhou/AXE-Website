# Create your views here.
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from page.models import LoginForm, RegisterForm, RegCode, Member
from resources.models import Exam, ExamForm, create_exam_path
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
    exams = Exam.objects.all()
    return render(request, BASE_DIR + '/exams.html', {'is_logged_in': request.user.is_authenticated(), 
                    'user_name': request.user, 'MEDIA_ROOT': settings.MEDIA_ROOT, 'BASE_URL': baseurl(request), 'exams': exams})

def upload_exam(request):
    if not request.user.is_authenticated():
        return redirect('/login')
    if request.method == 'POST':
        if 'logout' in request.POST:
            logout(request)
            return redirect('/login')
        print 'processing update'
        form = ExamForm(request.POST, request.FILES)    
        if form.is_valid():
            data = form.cleaned_data
            pdf_path = create_exam_path(data) 
            print Exam.objects.filter(pdf_path=pdf_path)
            if len(Exam.objects.filter(pdf_path=pdf_path)) > 0:
                return HttpResponse('<html><body>Sorry!</body></html>') 
            exam = Exam(instructor=data['instructor'], key=data['key'], term=data['term'], subject=data['subject'], \
                        course=data['course'], year=data['year'], exam=data['exam'], pdf_path=pdf_path)
            exam.save()
            exam_file = data['test']
            f = open(os.path.dirname(os.path.dirname(__file__)) + '/media/exams/' + pdf_path, 'w')
            f.write(exam_file.read())
            f.close()
            return HttpResponse('<html><body> Success! </body></html>')
    else:
        form = ExamForm() 
    print form
    return render(request, BASE_DIR + '/exam_upload.html', {'is_logged_in': request.user.is_authenticated(),
                    'user_name': request.user, 'form': form})

def baseurl(request):
    if request.is_secure():
        scheme = 'https://'
    else:
        scheme = 'http://'
    return scheme + request.get_host()
