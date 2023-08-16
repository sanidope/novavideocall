from . import views
from django.urls import path
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView,
    PasswordResetDoneView, PasswordResetConfirmView,
    PasswordResetCompleteView
)

app_name = 'account' 

urlpatterns = [
    path('auth/login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('auth/logout/', LogoutView.as_view(next_page='/'), name='logout'),
    
    path('auth/sign-up/', views.Register.as_view(), name='signup'),
    path('auth/sign-up/cont/', views.Register2.as_view(), name='signup2'),
    path('auth/sign-up/completed/', views.SignUpCompleted.as_view(), name='signup_completed'),
    path('auth/password-reset/', PasswordResetView.as_view(template_name='account/password_reset_form.html',
                                                           success_url='/account/auth/password-reset/done',
                                                           email_template_name='account/password_reset_email.html'),
                                                           name='forgotpassword'),
                                                           
    path('auth/password-reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html',
                                          success_url='/account/auth/password-reset/complete/'),
         name='password_reset_confirm'),

         
    path('auth/password-reset/complete/',
         PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),


    path('auth/password-reset/done', PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
        name='password_reset_done')


    

]
