from django.urls import path
from.views import StudentListView,TeacherDetailView,CourseListView,ClassesListView,CourseListView,ClassperiodListView,StudentDetailView

urlpatterns = [
    path("students/",StudentListView.as_view(),name = 'student_list_view'),
    path("teacher/",TeacherDetailView.as_view(),name = 'student_list_view'),
    path("period/",ClassperiodListView.as_view(),name = 'student_list_view'),
    path("classes/",ClassesListView.as_view(),name = 'student_list_view'),
    path("courses/",CourseListView.as_view(),name = 'student_list_view'),
    path("students/<int:id>/",StudentDetailView.as_view(),name = 'student_detail_view'),
    path("teacher/<int:id>/",TeacherDetailView.as_view(),name = 'student_detail_view'),
    path("period/<int:id>/",ClassperiodListView.as_view(),name = 'student_detail_view'),
    path("classes/<int:id>/",ClassesListView.as_view(),name = 'student_detail_view'),
    path("courses/<int:id>/",CourseListView.as_view(),name = 'student_detail_view'),


    
]