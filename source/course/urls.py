from django.urls import path

from course.views.course_favourite_views import CourseFavouriteCreateView
from course.views.course_order_views import CourseOrderView
from course.views.course_views import CourseListView, CourseDetailView, CourseUpdateView, CourseDeleteView, \
        CourseCreateView

app_name = 'course'


urlpatterns = [
        path('course/list/', CourseListView.as_view(), name='course_list_view'),
        path('course/create/', CourseCreateView.as_view(), name='course_create_view'),
        path('course/details/<int:pk>', CourseDetailView.as_view(), name='course_detail_view'),
        path('course/update/<int:pk>', CourseUpdateView.as_view(), name='course_update_view'),
        path('course/delete/<int:pk>', CourseDeleteView.as_view(), name='course_delete_view'),
        path('course/order/', CourseOrderView.as_view(), name='course_order'),
        path('course/favourite/<int:pk>', CourseFavouriteCreateView.as_view(), name='course_favourite_create_view'),
]



