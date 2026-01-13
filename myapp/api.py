from django.urls import path
from .views import *

urlpatterns = [
    path('tours/', tour_list,),
    path('bookings/',booking_list,),
    path('reviews/', review_list,),
    path('tours/<int:pk>/', tour_detail,),
    path('tours/<int:pk>/delete/', tour_delete,),
    path('bookings/<int:pk>/', booking_detail,),
    path('bookings/<int:pk>/delete/', booking_delete,),
    path('reviews/<int:pk>/', review_detail,),
    path('reviews/<int:pk>/delete/', review_delete,),
    
]
