from django.test import TestCase, Client
from django.contrib.auth.models import User
from booking.models import Facility, Booking
from datetime import date
from django.urls import reverse

class BookingViewsTest(TestCase):
    def setUp(self):
        """Set up test data before each test runs."""
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.facility = Facility.objects.create(name="Test Room", location="Building 1", capacity=10)

    def test_facility_list_view(self):
        """Test if facility list page loads correctly."""
        response = self.client.get(reverse("facility_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "booking/facility_list.html")

    def test_booking_creation(self):
        """Test if a logged-in user can create a booking."""
        self.client.login(username="testuser", password="testpass")
        
        # ✅ FIXED: Provide facility_id when reversing the URL
        response = self.client.post(reverse("book_facility", args=[self.facility.id]), {
            "facility": self.facility.id,
            "date": date.today(),
        })

        self.assertEqual(response.status_code, 302)  # Redirect after booking
        self.assertEqual(Booking.objects.count(), 1)
