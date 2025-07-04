# reselling/forms.py
from django import forms
from .models import ResellOrder

class OrderForm(forms.ModelForm):
    class Meta:
        model = ResellOrder
        fields = ['full_name', 'email', 'phone']
