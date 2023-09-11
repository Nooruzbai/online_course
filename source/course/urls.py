from django.urls import path

from course.views.course_views import CourseListView, CourseDetailView, CourseUpdateView, CourseDeleteView

app_name = 'course'


urlpatterns = [
        path('course/list/', CourseListView.as_view(), name='course_list_view'),
        path('course/details/<int:pk>', CourseDetailView.as_view(), name='course_detail_view'),
        path('course/update/<int:pk>', CourseUpdateView.as_view(), name='course_update_view'),
        path('course/delete/<int:pk>', CourseDeleteView.as_view(), name='course_delete_view'),
]

