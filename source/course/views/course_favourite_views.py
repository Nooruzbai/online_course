from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from course.models import Course


class CourseFavouriteCreateView(APIView):
    def post(self, request, pk):
        current_user = self.request.user
        course_pk = pk
        course = get_object_or_404(Course, pk=course_pk)
        course_favourites = course.favourites.all()
        if current_user not in course_favourites:
            course.favourites.add(current_user)
            return Response({
                "name": course.name,
                "status": "Favourited"

            }, status=status.HTTP_201_CREATED, content_type='application/json')
        else:
            course.favourites.remove(current_user)
            return Response({
                "name": course.name,
                "status": "Unfavourited"

            }, status=status.HTTP_201_CREATED, content_type='application/json')