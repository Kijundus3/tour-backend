from django.contrib import admin
from .models import Tour, Booking, Review

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'duration', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'price')
    ordering = ('-created_at',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'tour', 'booking_date')
    search_fields = ('customer_name', 'customer_email', 'tour__title')
    list_filter = ('booking_date',)
    ordering = ('-booking_date',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'tour', 'rating', 'created_at')
    search_fields = ('customer_name', 'tour__title', 'comment')
    list_filter = ('rating', 'created_at')
    ordering = ('-created_at',)
        


