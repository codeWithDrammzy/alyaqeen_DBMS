from django.urls import path
from . import views

urlpatterns = [
    path('add-student', views.add_student, name="add-student"),
    path('student-list', views.student_list, name="student-list"),
    path('student-detail/<int:pk>', views.student_detail, name="student-detail"),
]