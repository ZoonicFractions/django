from django.urls import path

from . import views

urlpatterns = [
    path('create-user', views.CreateUser.as_view(), name = 'create-user'),
    path('update-user', views.UpdateUser.as_view(), name = 'update-user'),
    path('update-userpassword', views.UpdateUserPassword.as_view(), name = 'update-userpassword'),
    path('delete-user/<str:username>', views.DeleteUser.as_view(), name = 'delete-user'),
    path('create-log', views.GameLogRegister.as_view(), name = 'create-log'),
    path('view-logs-student/<int:difficulty>/<str:classroom>/<int:role_number>/', views.ViewStudentLogs.as_view(), name = 'view-logs-student'),
    path('view-logs-student-chart/<int:difficulty>/<str:classroom>/<int:role_number>/<int:level>', views.ViewStudentLogsChart.as_view(), name = 'view-logs-student-chart'),
    path('level-participation-chart/<int:difficulty>/<str:classroom>', views.StudentPaticipation.as_view(), name = 'level-participation-chart'),
]