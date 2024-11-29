from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('classes/', views.classes, name='classes'),
    path('caracters/', views.caracters, name='caracters'),
    path('habilidades/', views.habilidades, name='habilidades')
]