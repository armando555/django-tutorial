from rest_framework import viewsets

from ..serializers import CourseSerializer
from ..models import Course

# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
