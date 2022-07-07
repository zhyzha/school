from rest_framework.validators import UniqueTogetherValidator

from courses_app.models import Course
from rest_framework import serializers


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'duration', 'price', 'is_active']

        #такое можно сделать с фронта будет поступать информация
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Course.objects.all(),
        #         fields=['name', 'duration', 'price']
        #     )
        # ]

