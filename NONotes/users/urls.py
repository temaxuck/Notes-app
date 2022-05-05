from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as users_views

urlpatterns = [
    path('register/', users_views.register, name='register'),
    path('login/', users_views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', users_views.profile, name='profile'),
]
