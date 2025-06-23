
from django.urls import path
from . import views

urlpatterns = [
    path('admin-dashboard/', views.admin_dashboard, name="admin-dashboard"),
    path('academic-session/', views.academic_session, name="academic-session"),
    path('add-subject', views.add_subject , name="add-subject"),
    path('staf-listf', views.staff_list , name="staff-list"),
    path('staff-id/<int:staff_id>/', views.staff_id, name='staff-id'),
    path('support-id/<int:staff_id>/', views.support_id, name='support-id'),
    path('support-staff', views.support_staff, name='support-staff'),

    path('remove-subject/<int:pk>', views.remove_subject , name="remove-subject"),

    #teachers
    path('add-teacher/', views.add_teacher, name="add-teacher"), 
    path('teacher-list/', views.teacher_list, name="teacher-list"), 
    path('teacher-detail/<int:pk>', views.teacher_detail, name="teacher-detail"), 
    path('edit-teacher/<int:pk>', views.edit_teacher, name="edit-teacher"),
    path('delete-teacher/<int:pk>', views.delete_teacher, name="delete-teacher"),
    path('logout-user/', views.logoutUser, name="logout-user"),
]


