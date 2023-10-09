from rest_framework import serializers

from course.models import Course, Order


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "name", "image", "description", "type", "price")


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("course",)


class CartCourseSerializer(CourseSerializer):
    quantity = serializers.IntegerField(required=True)

    class Meta:
        model = Course
        fields = ('quantity',)







