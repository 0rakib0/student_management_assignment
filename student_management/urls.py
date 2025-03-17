from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentList, name='student_list'),
    path('creates-student/', views.CreateStudent, name='create-student'),
    path('delete-student/<int:id>/', views.DeleteStudent, name='delete-student'),
    path('student-update/<int:id>/',views.UpdateStudent, name='update_stu')
]