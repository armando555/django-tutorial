from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=60)
    credits = models.PositiveSmallIntegerField()
    status = models.BooleanField(default= True)
    
    def get_name(self):
        return self.name
    
    def get_credits(self):
        return self.credits
    
    def get_status(self):
        return self.status
    
    def set_name(self, name: str):
        self.name = name
    
    def set_credits(self, credits: int):
        self.credits = credits    
        
    def set_status(self, status: bool):
        self.status = status
        
    def __str__(self):
        return f"{self.name} | {self.credits} | {self.status}"
    
    