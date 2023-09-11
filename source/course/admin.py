from django.contrib import admin

from course.models import Course


# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'price',]


admin.site.register(Course, CourseAdmin)
