from django.db import models
from datetime import date

# Create your models here.
class Student(models.Model):
    last_name = models.CharField(max_length=60)
    full_name = models.CharField(max_length=60)
    dni = models.CharField(max_length=12)
    birth_day = models.DateField()
    GENDERS = (('F', 'Female'),('M', 'Male'))
    gender = models.CharField(max_length=1,choices=GENDERS,default='M')
    
    def get_last_name(self):
        return self.last_name
    
    def get_full_name(self):
        return self.full_name
    
    def get_dni(self):
        return self.dni
    
    def get_birth_day(self):
        return self.birth_day
    
    def get_gender(self):
        return self.gender
    
    def set_last_name(self, last_name: str):
        self.last_name = last_name
    
    def set_full_name(self, full_name: str):
        self.full_name = full_name
    
    def set_dni(self, dni: str):
        self.dni = dni
        
    def set_birth_day(self, birth_day: date):
        self.birth_day = birth_day
    
    def set_gender(self, gender: str):
        self.gender = gender
        
    def __str__(self):
        return f"{self.dni} | {self.full_name} | {self.last_name} | {self.gender}"
    
    