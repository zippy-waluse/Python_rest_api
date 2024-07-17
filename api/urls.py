from django.urls import path
from.views import StudentListView,TeacherSerializer,ClassesSerializer,CoursesSerializer,ClassperiodSerializer

urlpatterns = [
    path("students/",StudentListView.as_view(),name = 'student_list_view'),
    path("teacher/",StudentListView.as_view(),name = 'student_list_view'),
    path("period/",StudentListView.as_view(),name = 'student_list_view'),
    path("classes/",StudentListView.as_view(),name = 'student_list_view'),
    path("courses/",StudentListView.as_view(),name = 'student_list_view'),
]