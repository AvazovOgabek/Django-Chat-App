from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('profile/<int:profile_id>/', views.profile_detail, name='profile_detail'),
    path('chat/<int:chat_id>/', views.chat, name='chat'),
    path('my-profile/', views.my_profile, name='my_profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('delete-chat/<int:chat_id>/', views.delete_chat, name='delete_chat'),

]