from django.contrib import admin
from .models import Facility, Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'facility', 'date', 'status')  # Show these fields
    list_filter = ('status',)  # Allow filtering by status
    actions = ['approve_booking', 'cancel_booking']  # Add admin actions

    def approve_booking(self, request, queryset):
        queryset.update(status='Confirmed')
    approve_booking.short_description = "Approve selected bookings"

    def cancel_booking(self, request, queryset):
        queryset.update(status='Canceled')
    cancel_booking.short_description = "Cancel selected bookings"

admin.site.register(Facility)
admin.site.register(Booking)