from courses_app.models import Course
from courses_app.serializers import CoursesSerializer
from rest_framework import viewsets


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    #ReadOnlyModelViewSet фронтэнд может лишь читать
    """info about courses"""
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer
