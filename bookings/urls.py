from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_booking, name='view_booking'),
    path('create-booking/', views.create_booking, name='create_booking'),
    path('edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
]
