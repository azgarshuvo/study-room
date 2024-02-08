from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('rooms/', views.getRooms),
    path('rooms/<str:pk>', views.getRoom),
    path('room-create/', views.createRoom),
    path('room-update/<str:pk>', views.updateRoom),
    path('room-delete/<str:pk>', views.deleteRoom),
]


