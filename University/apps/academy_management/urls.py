from django.urls import path,include
from rest_framework import routers
from .views import CourseViewSet, EnrollmentViewSet, StudentViewSet


router = routers.DefaultRouter()
router.register(r'students',viewset=StudentViewSet)
router.register(r'courses',viewset=CourseViewSet)
router.register(r'enrollments',viewset=EnrollmentViewSet)

urlpatterns=[
    path('',include(router.urls))
]