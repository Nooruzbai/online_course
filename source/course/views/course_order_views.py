from django.views.generic import CreateView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from course.models import Order
from course.serializers import OrderSerializer


class CourseOrderView(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(user_id = current_user.id)

