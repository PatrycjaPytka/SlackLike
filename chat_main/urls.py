from django.urls import path
from . import views

app_name='chat_main'

urlpatterns = [
    path('', views.index, name='index'),
    path('newgroup/<str:room_name>/', views.room, name='room'),
    path('newgroup/', views.new_group, name='new_group'),
    path('deletegroup/', views.delete_group, name='delete_group'),
    path('deletegroup/<str:group>/', views.confirm, name='confirm'),
    path('editgroup/<str:room_name>/', views.edit_group, name='edit_group'),
    path('leave_group/<str:group>/', views.leave_group, name='leave_group'),
    path('find_group/', views.find_group, name='find_group'),
]