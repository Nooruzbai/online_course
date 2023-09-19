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

    def perform_create(self, serializer):
        current_user = self.request.user
        order = serializer.save(user_id=current_user.id)
        return Response({
            "id": order.id,
            "name": order.course.name,
            "status": "Created"

        }, status=status.HTTP_201_CREATED, content_type='application/json')


