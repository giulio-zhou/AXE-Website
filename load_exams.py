from resources.models import Exam
f = open('exams.txt')
exam_contents = f.read().split('\n')
exam_contents.pop()
for elem in exam_contents:
	exam = elem.split('-')
	instructor = exam[3]
	if 'soln' in exam[4]:
		key = True
	else:
		key = False
	if exam[2] == 'mt1':
		exam_type = 'Midterm 1'
	elif exam[2] == 'mt2':
		exam_type = 'Midterm 2'
	else:
		exam_type = 'Final Exam'

	if 'fa' in exam[1]:
		term = 'Fall'
	elif 'sp' in exam[1]:
		term = 'Spring'
	else:
		term = 'Summer'

	pdf_path = elem
	year = int(exam[1][2:])
	if 'cheme' in exam[0]:
		subject = 'Chemical Engineering'
		course = exam[0][5:]
	elif 'chem' in exam[0]:
		subject = 'Chemistry'
		course = exam[0][4:]
	exam = 0
	print instructor, key, exam_type, term, pdf_path, year, subject, course
	Exam.objects.create(instructor=instructor, key=key, term=term, year=year, pdf_path=pdf_path, subject=subject, course=course, exam=exam_type)
print Exam.objects.all()
