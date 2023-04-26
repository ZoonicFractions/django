from django.urls import path, reverse_lazy
from . import views, forms
from django.contrib.auth import views as auth_views
from gameServer.settings import EMAIL_HOST_USER

# Create your urls here.
app_name = "zoonicWebsite"
urlpatterns = [
    path('', views.index, name='index'),
    path('gen-dif/<int:difficulty>', views.general, name='general'),
    path('A-dif/<int:difficulty>', views.classroomA, name='classroomA'),
    path('B-dif/<int:difficulty>', views.classroomB, name='classroomB'),
    path('<int:difficulty>/<str:classroom>/<int:role_number>/',
         views.dashboard, name='dashboard'),
    path('notfound', views.notfound, name='notfound'),
    path('log_in', views.log_in, name='log_in'),
    path('log_out', views.log_out, name='log_out'),
    path('read', views.readUsers, name='read'),
    path('updateDelete/<str:username>/',
         views.updateDeleteUser, name='updateDelete'),
    path('create', views.createUser, name='create'),
    path('download', views.download, name='download'),
    path('password_reset', auth_views.PasswordResetView.as_view(
            template_name='resetPassword/password_reset.html',
            form_class= forms.ResetForm,
            email_template_name='resetPassword/password_reset_email.html',
            from_email=EMAIL_HOST_USER,
            success_url = reverse_lazy("zoonicWebsite:password_reset_done"),
            html_email_template_name='resetPassword/password_reset_email.html'
        ), name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='resetPassword/password_reset_done.html'), 
        name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='resetPassword/password_reset_confirm.html',
        form_class=forms.RecoverPassword, 
        success_url = reverse_lazy("zoonicWebsite:password_reset_complete")), name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='resetPassword/password_reset_complete.html'), name='password_reset_complete'),
]
