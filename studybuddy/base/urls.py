from django.urls import path
from base.views import (
    deleteRoom,
    home,
    room,
    createRoom,
    updateRoom,
    deleteRoom,
    loginPage,
    logoutUser,
)


urlpatterns = [
    path("login/", loginPage, name='login'),
    path("logout/", logoutUser, name='logout'),
    path('', home, name='home'),
    path('room/<str:pk>/', room, name="room"),
    path('create-room/', createRoom, name='create-room'),
    path('update-room/<str:pk>/', updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', deleteRoom, name='delete-room'),
]
