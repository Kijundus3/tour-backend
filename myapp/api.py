from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
'''
urlpatterns = [

    
    path('tours/', tour_list,),
    path('bookings/',booking_list,),
    path('reviews/', review_list,),
    path('tours/<int:pk>/', tour_detail,),
    path('tours/<int:pk>/delete/', tour_delete,),
    path('tours/create/', tour_create,),
    path('tours/<int:pk>/update/', tour_update,),
    path('bookings/<int:pk>/', booking_detail,),
    path('bookings/<int:pk>/delete/', booking_delete,),
    path('bookings/create/', booking_create,),
    path('bookings/<int:pk>/update/', booking_update,),
    path('reviews/<int:pk>/', review_detail,),
    path('reviews/<int:pk>/delete/', review_delete,),
    path('reviews/create/', review_create,),
    path('reviews/<int:pk>/update/', review_update,),
     
]
'''


urlpatterns = [
    path('tours/', manage_tour),
    path('tours/<int:id>/', manage_tour),
    path('bookings/', manage_booking),
    path('bookings/<int:id>/', manage_booking),
    path('reviews/', manage_review),
    path('reviews/<int:id>/', manage_review),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]