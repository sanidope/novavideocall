from . import views
from django.urls import path 

app_name = 'api'


urlpatterns = [

    path('<int:id_token>/', views.update_installed_app, name='installed_status')
]