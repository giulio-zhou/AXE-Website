from django.contrib import admin
from resources.models import Exam

def approve_exam(modeladmin, request, queryset):
    queryset.update(approved=True)
approve_exam.short_description = "Mark following exams as approved"

class ExamAdmin(admin.ModelAdmin):
    list_display = ['instructor', 'key', 'term', 'subject', 'course', \
                    'year', 'exam', 'approved']
    ordering = ['course']
    actions = [approve_exam]

admin.site.register(Exam, ExamAdmin)
