from django.db import models
from .student import Student
from .course import Course


# Create your models here.
class Enrollment(models.Model):
    student_id_fk = models.ForeignKey(Student, null=False, blank=False, on_delete=models.CASCADE)
    course_id_fk = models.ForeignKey(Course, null=False, blank=False, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"{self.student_id_fk} | {self.course_id_fk} | {self.enrollment_date}"
    
    