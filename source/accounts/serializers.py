from django.contrib.auth import get_user_model
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from accounts.models import Profile
from course.models import Course
from course.serializers import CourseSerializer

User = get_user_model()


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'phone_number')


class UserSerializer(ModelSerializer):
    favourites = SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'profile', 'favourites')

    # def update(self, instance, validated_data):
    #     userprofile_serializer = self.fields['profile']
    #     userprofile_instance = instance.userprofile
    #     userprofile_data = validated_data.pop('userprofile', {})
    #
    #     # to access the UserProfile fields in here
    #     # mobile = userprofile_data.get('mobile')
    #
    #     # update the userprofile fields
    #     userprofile_serializer.update(userprofile_instance, userprofile_data)
    #
    #     instance = super().update(instance, validated_data)
    #     return instance

    def get_favourites(self, obj):
        return obj.favourite.all()



