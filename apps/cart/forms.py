import re

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.core.exceptions import ValidationError


def only_number(value):
    if not re.match('^[0-9 ]+$', value):
        raise ValidationError('It should contains only digits')


class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    phone_number = forms.CharField(max_length=15)
    country = forms.CharField(max_length=100)
    town_city = forms.CharField(max_length=150)
    postcode = forms.CharField(min_length=4, max_length=6, validators=[only_number])
    address_line_1 = forms.CharField(max_length=150)
    address_line_2 = forms.CharField(max_length=150, required=False)
    # Payment
    credit_card = forms.CharField(min_length=10, max_length=20, validators=[only_number])
    cvv = forms.CharField(min_length=3, max_length=3, validators=[only_number])

    def __init__(self, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = "."
        self.helper.add_input(Submit('submit', 'Confirm and pay', css_class="button is-dark is-uppercase"))
