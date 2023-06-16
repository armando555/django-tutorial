from rest_framework import serializers
from ..models import Student

# Create your models here.
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


    
    