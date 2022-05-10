from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as users_views

urlpatterns = [
    path('register/', users_views.register, name='register'),
    path('login/', users_views.login, name='login'),
    path('logout/', users_views.signout, name='signout'),
    path('profile/', users_views.profile, name='profile'),
]
