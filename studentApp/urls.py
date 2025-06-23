from django.urls import path
from . import views

urlpatterns = [
    path('add-student', views.add_student, name="add-student"),
    path('student-detail/<int:pk>', views.student_detail, name="student-detail"),
    path('edit-student/<int:pk>', views.edit_student, name="edit-student"),
    path('senior-class', views.seniorclass, name="senior-class"),
    path('junior-class', views.juniorclass, name="junior-class"),
    path('primary-class', views.primaryclass, name="primary-class"),
    path('nursery-class', views.nurseryclass, name="nursery-class"),





    path('delete-student<int:pk>', views.delete_student, name="delete-student"),
]