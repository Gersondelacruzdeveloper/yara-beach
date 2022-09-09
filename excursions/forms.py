
from django.forms import ModelForm
from django import forms
from .models import Excursions

# Gets a already made form  and add the new excursion
class AddExcursionForm(ModelForm):
    class Meta:
        model = Excursions
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(AddExcursionForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': ' Add title'})
        self.fields['Price'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add price..'})
        self.fields['image_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add an image name'})