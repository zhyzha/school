from students.models import Student
from students.serializers import StudentsSerializer
from rest_framework import viewsets

class StudentsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer

