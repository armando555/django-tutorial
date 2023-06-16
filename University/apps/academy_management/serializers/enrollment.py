from rest_framework import serializers
from ..models import Enrollment

# Create your models here.
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'


    
    