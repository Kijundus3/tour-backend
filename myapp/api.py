from django.urls import path
from .views import *

urlpatterns = [
    path('tours/', tour_list,),
    path('bookings/',booking_list,),
    path('reviews/', review_list,),
    path('tours/<int:pk>/', tour_detail,),
    path('tours/<int:pk>/delete/', tour_delete,),
]
