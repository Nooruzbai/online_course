from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveUpdateAPIView

# from accounts.serializers import UserSerializer

User = get_user_model()



# Create your views here.

# class UserAPIView(RetrieveUpdateAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     # permission_classes = (IsAuthenticated,)
#
#     def get_object(self):
#         return self.request.user