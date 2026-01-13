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

# Get Booking by ID
@api_view(['GET'])
def booking_detail(request, pk):
    try:
        booking = Booking.objects.get(pk=pk)
    except Booking.DoesNotExist:
        return Response({'error': 'Booking not found'}, status=404)
    
    serializer = BookingSerializer(booking)
    return Response(serializer.data)

# Delete Booking by ID
@api_view(['DELETE'])
def booking_delete(request, pk):
    try:
        booking = Booking.objects.get(pk=pk)
    except Booking.DoesNotExist:
        return Response({'error': 'Booking not found'}, status=404)

    booking.delete()
    return Response({'message': 'Booking deleted successfully'}, status=204)



# REVIEWS API VIEWS
@api_view(['GET'])    
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

# Get Review by ID
@api_view(['GET'])
def review_detail(request, pk):
    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        return Response({'error': 'Review not found'}, status=404)
    
    serializer = ReviewSerializer(review)
    return Response(serializer.data)

# Delete Review by ID
@api_view(['DELETE'])
def review_delete(request, pk): 
    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        return Response({'error': 'Review not found'}, status=404)

    review.delete()
    return Response({'message': 'Review deleted successfully'}, status=204)  

