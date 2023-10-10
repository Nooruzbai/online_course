from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from course.models import Order
from course.serializers import OrderSerializer


class CourseOrderView(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'Message': 'You have successfully bought the course'}, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        current_user = self.request.user
        order = serializer.save(user_id=current_user.id)
        return order