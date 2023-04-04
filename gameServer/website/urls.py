from django.urls import path, include
from . import views

# Create your urls here.
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<str:classroom>/<int:role_number>/', views.dashboard, name = 'dashboard'),
    path('forget-password', views.forget_password, name='forget-password'),
    path('recover', views.recover, name='recover'),
]