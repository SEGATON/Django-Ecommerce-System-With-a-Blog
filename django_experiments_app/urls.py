from django.urls import path
from . import views  

app_name = 'django_experiments_app'

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('', views.index, name='index'),

]
