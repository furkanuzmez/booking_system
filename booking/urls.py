from django.urls import path
from .views import FacilityListView, BookFacilityView, BookingListView, RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Updated for CBV
    path('', FacilityListView.as_view(), name="facility_list"),  # Facility List
    path('book/<int:facility_id>/', BookFacilityView.as_view(), name="book_facility"),  # Booking
    path('my-bookings/', BookingListView.as_view(), name="booking_list"),  # My Bookings
]
