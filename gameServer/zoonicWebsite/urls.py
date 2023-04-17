from django.urls import path, include
from . import views

# Create your urls here.
app_name = "zoonicWebsite"
urlpatterns = [
    path('gen-dif/<int:difficulty>', views.general, name = 'general'),
    path('A-dif/<int:difficulty>', views.classroomA, name = 'classroomA'),
    path('B-dif/<int:difficulty>', views.classroomB, name = 'classroomB'),
    path('<int:difficulty>/<str:classroom>/<int:role_number>/', views.dashboard, name = 'dashboard'),
    path('notfound', views.notfound, name = 'notfound'),
    path('', views.log_in, name = 'log_in'),
    path('crud', views.crud, name = 'crud'),
]