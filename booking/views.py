from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm  # Use Django's built-in form
from django.contrib.auth.models import User
from .models import Facility, Booking
from .forms import BookingForm

# Facility List (ListView)
class FacilityListView(ListView):
    model = Facility
    template_name = "booking/facility_list.html"
    context_object_name = "facilities"

class BookFacilityView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "booking/book_facility.html"
    success_url = reverse_lazy("booking_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        facility_id = self.kwargs.get("facility_id")
        facility = get_object_or_404(Facility, id=facility_id)
        kwargs["facility"] = facility  # Pass facility to the form
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["facility"] = get_object_or_404(Facility, id=self.kwargs.get("facility_id"))  # Pass facility to template
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.facility = get_object_or_404(Facility, id=self.kwargs.get("facility_id"))
        return super().form_valid(form)



class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "booking/booking_list.html"
    context_object_name = "bookings"

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)  # Show only current user's bookings



class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm  # Use Django's default user registration form
    template_name = "booking/register.html"
    success_url = reverse_lazy('facility_list')  # Redirect after successful registration

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # Log in the new user
        return response
