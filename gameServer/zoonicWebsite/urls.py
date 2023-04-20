from django.urls import path, include
from . import views

# Create your urls here.
app_name = "zoonicWebsite"
urlpatterns = [
    path('', views.index, name = 'index'),
    path('gen-dif/<int:difficulty>', views.general, name = 'general'),
    path('A-dif/<int:difficulty>', views.classroomA, name = 'classroomA'),
    path('B-dif/<int:difficulty>', views.classroomB, name = 'classroomB'),
    path('<int:difficulty>/<str:classroom>/<int:role_number>/', views.dashboard, name = 'dashboard'),
    path('notfound', views.notfound, name = 'notfound'),
    path('log_in', views.log_in, name = 'log_in'),
    path('log_out', views.log_out, name = 'log_out'),
    path('read', views.readUsers, name = 'read'),
    path('updateDelete/<str:username>/', views.updateDeleteUser, name = 'updateDelete'),
    path('create', views.createUser, name = 'create'),
    path('resetPassword', views.resetPassword, name="resetPassword"),
    path('download', views.download, name = 'download'),
]