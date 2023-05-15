from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'brand', 'price')

    def __init__(self):
        super().__init__()