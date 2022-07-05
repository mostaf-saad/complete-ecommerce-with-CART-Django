from django import forms
from .models import Order






class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name','mobile_number', 'email', 'address', 'city']