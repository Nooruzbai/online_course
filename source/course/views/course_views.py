from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView

from course.models import Course
from course.serializers import CourseSerializer


# Create your views here.

class CourseListView(ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseCreateView(CreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseDetailView(RetrieveAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseUpdateView(UpdateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseDeleteView(DestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
