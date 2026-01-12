from rest_framework import serializers
from .models import *



class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'




class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
