from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from products.models import Product


class StripeSubscriptionForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name',
                 'stripe_product_id',
                 'price',
                 'stripe_product_mode'
                  ]

    def __init__(self, *args, **kwargs):
        super().__init__()
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))
