from django.test import TestCase
from booking.forms import BookingForm
from booking.models import Facility
from datetime import date

class BookingFormTest(TestCase):
    def setUp(self):
        """Set up test data before each test runs."""
        self.facility = Facility.objects.create(name="Test Room", location="Building 1", capacity=10)

    def test_valid_booking_form(self):
        """Test if a valid BookingForm passes validation."""
        form = BookingForm(data={"facility": self.facility.id, "date": date.today()})
        self.assertTrue(form.is_valid())

    def test_invalid_booking_form(self):
        """Test if an invalid BookingForm (empty data) fails validation."""
        form = BookingForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("date", form.errors)
