from django import forms
from .models import Reference

class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = '__all__'
        exclude = ['user', 'has_due_payment', 'due_to_pay_amount', 'paid_amount','reference_number']