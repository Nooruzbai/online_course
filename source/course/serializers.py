from rest_framework import serializers

from source.course.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "name", "image", "description", "type", "price")

