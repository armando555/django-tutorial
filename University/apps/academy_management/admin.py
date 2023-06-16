from django.contrib import admin

# Register your models here.
from apps.academy_management.models import Course,  Enrollment, Student

admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Student)

