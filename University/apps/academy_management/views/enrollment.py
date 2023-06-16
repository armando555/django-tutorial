from rest_framework import viewsets

from ..serializers import EnrollmentSerializer
from ..models import Enrollment

# Create your views here.
class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
