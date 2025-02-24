from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Booking,Facility
from datetime import date

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["date"]  # Facility is pre-selected, so we remove it from the form

    def __init__(self, *args, **kwargs):
        facility = kwargs.pop("facility", None)
        super().__init__(*args, **kwargs)

        # Apply Flatpickr DatePicker
        self.fields["date"].widget = forms.TextInput(
            attrs={"class": "form-control datepicker", "placeholder": "Select a date"}
        )

        if facility:
            self.fields["facility"] = forms.ModelChoiceField(
                queryset=Facility.objects.filter(id=facility.id),
                initial=facility,
                disabled=True,
                widget=forms.HiddenInput()
            )


