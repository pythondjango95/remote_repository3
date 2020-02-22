from django import forms

from accounts.models import Products
from .models import Orders

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
class ProductForm(forms.ModelForm):
    class Meta:
        model =Products
        fields = '__all__'
