from django.contrib import admin
from courses_app.models import Course
from students.models import Student

admin.site.register(Course)
admin.site.register(Student)
