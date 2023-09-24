from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Course(models.Model):
    name = models.CharField(max_length=100, null=False,
                            blank=False, verbose_name='Name')
    image = models.ImageField(null=True, blank=True,
                              upload_to="images/course/")
    description = models.TextField(max_length=1000, null=True,
                                   blank=True, verbose_name='Description')
    type = models.IntegerField(default=0, blank=False,
                               null=False, verbose_name="Type")
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                blank=True, null=True, verbose_name="Price")
    date_created = models.DateTimeField(auto_now_add=True,
                                        verbose_name="Date created")
    date_edited = models.DateTimeField(auto_now_add=True,
                                       verbose_name="Date edited")
    user = models.ManyToManyField(User, related_name='courses', verbose_name="User")
    favourites = models.ManyToManyField(User, related_name='favourite', verbose_name='Favourite')

    def __str__(self):
        return f'{self.pk}. {self.name}, {self.name}'

    class Meta:
        db_table = 'course'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['id']


class Order(models.Model):
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, related_name='course_orders', verbose_name='Course id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_orders', verbose_name='User id')
    date_started = models.DateTimeField(auto_now=True, verbose_name='Date started')

    class Meta:
        db_table = 'order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['id']