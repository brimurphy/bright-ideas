from django import forms
from profiles.models import UserProfile


class BookingForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('full_name', 'cust_email', 'default_phone_number',
                  'date', 'default_street_address1', 'default_street_address2',
                  'default_town_or_city', 'default_county',)

    full_name = forms.CharField(max_length=254,)
    cust_email = forms.EmailField()
    comments = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Additional Comments...',
    }),)
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control date-time-picker-input',
            'data-target': '#date-time-picker'
        })
    )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes
        Remove labels and set autofocus to first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Name',
            'cust_email': 'Email',
            'date': 'Choose available date',
            'default_phone_number': 'Phone No.',
            'default_street_address1': 'Street Address',
            'default_street_address2': 'Street Address',
            'default_town_or_city': 'Town or City',
            'default_county':  'County',
            'comments': 'Additional Comments...',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'my-2')
            self.fields[field].label = False
