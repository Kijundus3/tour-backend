from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# First views.py file

'''
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


# Post Tours
@api_view(['POST'])
def tour_create(request):
    serializer = TourSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)




# Put Tours
@api_view(['PUT'])
def tour_update(request, pk):
    try:
        tour = Tour.objects.get(pk=pk)
    except Tour.DoesNotExist:
        return Response({'error': 'Tour not found'}, status=404)

    serializer = TourSerializer(tour, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)





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

# post Bookings
@api_view(['POST'])
def booking_create(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Put Bookings
@api_view(['PUT'])    
def booking_update(request, pk):
    try:
        booking = Booking.objects.get(pk=pk)
    except Booking.DoesNotExist:
        return Response({'error': 'Booking not found'}, status=404)

    serializer = BookingSerializer(booking, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


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

# Post Reviews
@api_view(['POST'])
def review_create(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Put Reviews
@api_view(['PUT'])
def review_update(request, pk):
    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        return Response({'error': 'Review not found'}, status=404)

    serializer = ReviewSerializer(review, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)        


'''
# Second views.py file


def generic_api(model_class, serializer_class):
    @api_view(['GET','POST', 'DELETE', 'PUT'])
    # @permission_classes([IsAuthenticated, IsAdminUser])
    def api(request, id = None):
        if request.method == 'GET':
            if id:
                try:
                    instance = model_class.objects.get(id = id)
                    serializer = serializer_class(instance)
                    return Response(serializer.data)
                except model_class.DoesNotExist:
                    return Response({'message':'Object Not Found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                instance = model_class.objects.all()
                serializer = serializer_class(instance, many = True)
                return Response(serializer.data)
            
        elif request.method == 'POST':
            serializer = serializer_class(data = request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        
        elif request.method == 'DELETE':
            if id:
                try:
                    instance = model_class.objects.get(id = id)
                    instance.delete()
                    return Response({'message':'Delete Successfully'})
                except model_class.DoesNotExist:
                    return Response({'message':'Object Not Found'})
                

        elif request.method == 'PUT':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    serializer = serializer_class(instance, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                
                        
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'})

    return api



manage_tour = generic_api(Tour, TourSerializer)
manage_booking = generic_api(Booking, BookingSerializer)
manage_review = generic_api(Review, ReviewSerializer)
