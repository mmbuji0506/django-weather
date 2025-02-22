from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('add-favorite-city/', views.add_favorite_city, name='add_favorite_city'),
    path('favorite-cities/', views.favorite_cities, name='favorite_cities'),
]