from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse


# from .views import login_view, logout_view
from .views import (
    home_view,
    create_event_view,
    book_event_view,
    booked_events_view,
    profile_view,
    login_view,
    logout_view,
)
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('create/', views.create_event_view, name='create_event'),       
    path('book/<int:event_id>/', views.book_event_view, name='book_event'),
    path('booked/', views.booked_events_view, name='booked_events'),
    path('profile/', views.profile_view, name='profile'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    
]








