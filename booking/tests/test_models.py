from django.test import TestCase
from django.contrib.auth.models import User
from booking.models import Facility, Booking
from datetime import date

class FacilityModelTest(TestCase):
    def test_facility_creation(self):
        """Test if a Facility is created correctly."""
        facility = Facility.objects.create(name="Test Room", location="Main Building", capacity=20)
        self.assertEqual(str(facility), "Test Room")

class BookingModelTest(TestCase):
    def setUp(self):
        """Set up test data before each test runs."""
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.facility = Facility.objects.create(name="Test Room", location="Building 1", capacity=10)

    def test_create_booking(self):
        """Test if a Booking is created correctly."""
        booking = Booking.objects.create(user=self.user, facility=self.facility, date=date.today())
        self.assertEqual(Booking.objects.count(), 1)
