from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('classes/', views.classes, name='classes'),
    path('races/', views.races, name='races'),
    path('characters/', views.characters, name='characters'),
    path('habilidades/', views.habilidades, name='habilidades'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create_character/', views.create_character, name='create_character'),
    path('get-classe-info/<int:classe_id>/', views.get_classe_info, name='get_classe_info'),
    path('delete_character/<int:character_id>/', views.delete_character, name='delete_character'),
]