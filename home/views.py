from django.shortcuts import redirect, render
from excursions.models import Excursions
from rentals.models import Rentals

# Create your views here.

# show excursions and rentals in home page
def home(request):
    excursions = Excursions.objects.all()[:4]
    rentals = Rentals.objects.all()[:4]
    context = {'excursions': excursions, 'rentals':rentals}
    return render(request, 'home.html', context)

from django.shortcuts import render
from excursions.models import Excursions
from rentals.models import Rentals
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage

# Create your views here.

# show excursions and rentals in home page
def home(request):
    excursions = Excursions.objects.all()[:4]
    rentals = Rentals.objects.all()[:4]
    context = {'excursions': excursions, 'rentals':rentals}
    return render(request, 'home.html', context)


# Contact form
def contact(request):
    if request.method == 'POST':
        template = render_to_string('email_templates.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['gersondelacruzdeveloper@gmail.com']
        )

        email.fail_silently = False
        email.send()
        return redirect('comfirmation')
    return render(request, 'contact.html')


# email comfirmation  for user
def email_comfirmation_page(request):
    return render(request, 'email_comfirmation.html')