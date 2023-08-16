from . import views 
from django.urls import path 


app_name = 'dashboard' 


urlpatterns = [

    path('settings/', views.settings, name='settings')
]