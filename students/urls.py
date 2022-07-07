from django.urls import path
from students.views import StudentsViewSet

urlpatterns = [
    path('', StudentsViewSet.as_view({'get': 'list'}), name='student-list'),
]