from django.contrib.auth import get_user_model
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from accounts.models import Profile
from course.serializers import OrderSerializer, CourseSerializer

User = get_user_model()


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'phone_number')


class UserSerializer(ModelSerializer):
    user_orders = OrderSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'profile', 'user_orders', 'favourite')

    def update(self, instance, validated_data):
        userprofile_serializer = self.fields['profile']
        userprofile_instance = instance.userprofile
        userprofile_data = validated_data.pop('userprofile', {})

        # to access the UserProfile fields in here
        # mobile = userprofile_data.get('mobile')

        # update the userprofile fields
        userprofile_serializer.update(userprofile_instance, userprofile_data)

        instance = super().update(instance, validated_data)
        return instance