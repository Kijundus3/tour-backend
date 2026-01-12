from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tour, Booking, Review
from .serializer import TourSerializer, BookingSerializer, ReviewSerializer

# Create your views here.
# TOURS API VIEWS
@api_view(['GET'])
def tour_list(request):
    tours = Tour.objects.all()
    serializer = TourSerializer(tours, many=True)
    return Response(serializer.data)

# Get Tour by ID
@api_view(['GET'])
def tour_detail(request, pk):
    try:
        tour = Tour.objects.get(pk=pk)
    except Tour.DoesNotExist:
        return Response({'error': 'Tour not found'}, status=404)
    
    serializer = TourSerializer(tour)
    return Response(serializer.data)


# Delete Tour by ID
@api_view(['DELETE'])
def tour_delete(request, pk):
    try:
        tour = Tour.objects.get(pk=pk)
    except Tour.DoesNotExist:
        return Response({'error': 'Tour not found'}, status=404)

    tour.delete()
    return Response({'message': 'Tour deleted successfully'}, status=204)


# BOOKINGS API VIEWS
@api_view(['GET'])
def booking_list(request):
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)


# REVIEWS API VIEWS
@api_view(['GET'])    
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


# Test