from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE, verbose_name='Profile')
    bio = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Bio')
    phone_number = PhoneNumberField(max_length=50, null=True, blank=True, unique=True, verbose_name="Phone number")

    class Meta:
        db_table = 'profile'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f"Profile: {self.id, self.user}"
