from django.forms import ModelForm
from django import forms
from excursions.models import Excursions, Photos,Reference
from .models import Post
from rentals.models import Rentals
from rentals.models import Photos as Rental_photos
from checkout.models import ExcursionOrder

# Gets a already made form  and add the new excursion
# class AddManualBookingForm(ModelForm):
#     class Meta:
#         model = ExcursionOrder
#         fields = '__all__'
#         exclude = ['user']
        
from datetime import datetime
from django import forms

class AddManualBookingForm(forms.ModelForm):
    custom_excursion_date = forms.DateField(
        label='Excursion Date',
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d', '%d-%m-%y'],  # Add more formats if needed
        required=True
    )

    class Meta:
        model = ExcursionOrder
        fields = '__all__'
        exclude = ['user', 'excursion_date']

    def clean_custom_excursion_date(self):
        # Convert the date format from 'dd-mm-yy' to 'YYYY-MM-DD'
        raw_date = self.cleaned_data.get('custom_excursion_date')
        if raw_date:
            try:
                converted_date = datetime.strptime(raw_date.strftime('%d-%m-%y'), '%d-%m-%y').strftime('%Y-%m-%d')
                return converted_date
            except ValueError:
                raise forms.ValidationError('Invalid date format. Please use dd-mm-yy.')

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.excursion_date = self.cleaned_data['custom_excursion_date']
        if commit:
            instance.save()
        return instance


# Gets a already made form  and add the new excursion
class ExcursionForm(ModelForm):
    class Meta:
        model = Excursions
        fields = '__all__'
        exclude = ['user', 'type_dropdown', 'slugy']

    def __init__(self, *args, **kwargs):
        super(ExcursionForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': ' Add title'})
        self.fields['price'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add price..'})
        self.fields['image_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add an image name'})
        
    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')

        if not description:
            self.add_error('description', 'Please provide a description.')

        return cleaned_data


# Gets a already made form and add the new excursion photos
class ExcursionFormPhotos(ModelForm):
    class Meta:
        model = Photos
        fields = ['images']


# Gets a already made form and add the new rental
class RentalForm(ModelForm):
    class Meta:
        model = Rentals
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(RentalForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': ' Add title'})
        self.fields['price'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add price..'})
        self.fields['image_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add an image name'})


# Gets a already made form and add the new rental photos
class RentalFormPhotos(ModelForm):
    class Meta:
        model = Rental_photos
        fields = ['images']


# Gets a already made form and add the new rental photos
class SellerForm(ModelForm):
    class Meta:
        model = Reference
        fields = '__all__'


# Gets a already made form and add the new rental photos
class OrderForm(ModelForm):
    class Meta:
        model = ExcursionOrder
        fields = '__all__'


# Gets a already made form  and add the new excursion
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user','date_posted', 'slug']

    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     self.fields['title'].widget.attrs.update(
    #         {'class': 'form-control', 'placeholder': ' Add title'})
    #     self.fields['price'].widget.attrs.update(
    #         {'class': 'form-control', 'placeholder': 'Add price..'})
