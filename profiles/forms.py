from django import forms

from .models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes
        Remove labels and set autofocus to first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone No.',
            'default_street_address1': 'Street Address',
            'default_street_address2': 'Street Address',
            'default_town_or_city': 'Town or City',
            'default_county':  'County',
            'default_postcode': 'Postcode',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'my-2')
            self.fields[field].label = False
