from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from profiles.models import UserProfile


def date_validate(date):
    if date <= timezone.now():
        raise ValidationError(
            "Great Scott!! That date is past,\
                please select a future time")


class BookingForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('default_full_name', 'default_email', 'default_phone_number',
                  'default_street_address1', 'default_street_address2',
                  'default_town_or_city', 'default_county',
                  'date', 'comments',)

    comments = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Additional Comments...',
    }),)
    date = forms.DateTimeField(
        validators=[date_validate],
        input_formats=['%DD/%MM/%YYYY %HH:%mm'],
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control date-time-picker-input',
            'data-target': '#date-time-picker',
        }),
    )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes
        Remove labels and set autofocus to first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Name',
            'default_email': 'Email',
            'default_phone_number': 'Phone No.',
            'default_street_address1': 'Street Address',
            'default_street_address2': 'Street Address',
            'default_town_or_city': 'Town or City',
            'default_county':  'County',
            'date': 'Choose available date',
            'comments': 'Additional Comments...',
        }

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'my-2')
            self.fields['comments'].required = False
            self.fields['default_street_address2'].required = False
            if field != 'date':
                self.fields[field].label = False
            else:
                self.fields[field].label = (
                    'Choose your preferred time and date')
