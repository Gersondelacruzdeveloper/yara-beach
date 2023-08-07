from django import forms
from .models import Reference

class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = ['full_name', 'bank_name','account_number', 'bank_acount_type', 'cedula']
