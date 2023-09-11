from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Course(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')
    image = models.ImageField(null=True, blank=True, upload_to="images/course/")
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Description')
    type = models.IntegerField(default=0, blank=False, null=False, verbose_name="Type")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Price")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    date_edited = models.DateTimeField(auto_now_add=True, verbose_name="Date edited")
    user = models.ManyToManyField(User, related_name='course', verbose_name="User")

    def __str__(self):
        return f'{self.pk}. {self.name}, {self.name}'

    class Meta:
        db_table = 'course'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['id']
