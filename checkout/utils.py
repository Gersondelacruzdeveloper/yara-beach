from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from datetime import date
from .models import ExcursionOrder
from django.shortcuts import redirect

def send_booking_email(request, guest_email=None):
    if request.user.is_authenticated:
        user_orders = ExcursionOrder.objects.filter(user=request.user)
    else:
        user_orders = ExcursionOrder.objects.filter(customer_email=guest_email)

    user_orders = user_orders.filter(date_created=date.today())
    excursion_total = 0

    thanks_booking = "<h2 style='background-color:#f85a15; padding: 10px; color:#ffffff;'>Thank you for booking with us</h2><hr>"
    subtitle = "<h3>Here are your bookings from today</h3>"
    template = thanks_booking + subtitle

    for item in user_orders:
        excursion_total += item.subtotal
        template += f"<p><strong>Item Name:</strong>{item.excursion_name[:25].title()}</p>"
        template += f"<img src='{item.image}' alt='{item.excursion_name}' style='object-fit:cover' width='200' height='200'><br/>"
        template += f"<strong>Excursion Date:</strong> {item.excursion_date}<br/>"
        template += f"<strong>Excursion Time:</strong> {item.time_selected}<br/>"
        template += f"<strong>Adult Quantity:</strong> {item.adult_qty}<br/>"
        if item.child_qty:
            template += f"<strong>Child Quantity:</strong> {item.child_qty}<br/>"
        if item.infant_qty:
            template += f"<strong>Infant Quantity:</strong> {item.infant_qty}<br/>"
        template += f"<strong>Pick up:</strong> {item.place_pickup} <br/>"
        template += f"<strong>Excursion Booking Number:</strong> {item.order_number} <br/>"
        template += f"<strong>SubTotal:</strong> {item.subtotal} <hr>"

    template += f"<strong style='background-color:#f85a15; padding: 10px; color:#ffffff;'>Amount Paid:</strong> ${excursion_total} <hr>"

    email = EmailMultiAlternatives(
        'From Punta Cana Explore',
        template,
        settings.EMAIL_HOST_USER,
        [guest_email, 'puntacanaexploregt@gmail.com']
    )
    email.attach_alternative(template, "text/html")
    email.fail_silently = False
    email.send()


# sendfing email to seller
def send_email_to_seller(request, extracted_reference, checkout_cart):
    template_for_seller = ''
    
    if extracted_reference:
        for e in extracted_reference:
            e.due_to_pay_amount += checkout_cart.get('total_adult', 0) * 10
            e.paid_amount += checkout_cart.get('total_adult', 0) * 10
            e.save()

            template_for_seller += f"<h2 style='background-color:#f85a15; padding: 10px; color:#ffffff;'>¡Felicidades, {e.full_name}!</h2><hr>"
            template_for_seller += f"<p>Queríamos informarte que has ganado ${e.due_to_pay_amount} por la venta exitosa de excursión. Tu arduo trabajo está dando frutos.</p>"
            template_for_seller += f"<p>El dinero estará en tu cuenta ******{e.account_number[-4:]} en menos de 4 días, a menos que el cliente cancele la reserva.</p>"
            template_for_seller += "<p>¡Sigue así!</p>"
            template_for_seller += "<p>Saludos</p>"
            template_for_seller += "<p>Punta Cana Explore</p>"

            email = EmailMultiAlternatives(
                'From Punta Cana Explore for sellers',
                template_for_seller,
                settings.EMAIL_HOST_USER,
                [e.email]
            )

            email.attach_alternative(template_for_seller, "text/html")
            email.fail_silently = False
            email.send()

    # Empty the cart when payment has been processed
    request.session['cart'] = {}
    return redirect('checkout-success')