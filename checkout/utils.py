from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from datetime import date
from .models import ExcursionOrder
from django.shortcuts import redirect
from decimal import Decimal,ROUND_HALF_UP

def send_booking_email(cart_content,order_number,pay_at_pickup, anticipo,guest_email=None,):
    thanks_booking = "<h2 style='background-color:#f85a15; padding: 10px; color:#ffffff;'>Thank you for booking with us</h2><hr>"
    subtitle = "<h3>Here are your bookings from today</h3><hr>"
    warning = '<h4 style="color:red;">Please be aware that this is the advance payment, and the remaining amount will need to be paid upon pick-up.</h4>'
    template = thanks_booking + subtitle + warning

    for item in cart_content['cart_items']:
        print('cart_content', cart_content)
        template += f"<p><strong>Item Name:</strong>{item['excursion'].title}</p>"
        template += f"<img src='{item['excursion'].main_image.url}' alt='{item['excursion'].title}' style='object-fit:cover' width='200' height='200'><br/>"
        template += f"<strong>Excursion Date:</strong> {item['values']['excursion_date']}<br/>"
        template += f"<strong>Excursion Time:</strong> {item['values']['selected_time']}<br/>"
        template += f"<strong>Adult Quantity:</strong>{item['values']['adult_qty']}<br/>"
        if item['values']['child_qty']:
            template += f"<strong>Child Quantity:</strong> {item['values']['child_qty']}<br/>"
        if item['values']['infant_qty']:
            template += f"<strong>Infant Quantity:</strong> {item['values']['infant_qty']}<br/>"
        template += f"<strong>Pick up:</strong> {item['values']['place_pickup']} <br/>"
        if item['values']['place_dropup']:
            template += f"<strong>Drop Off:</strong> {item['values']['place_dropup']} <br/>"
        template += f"<strong>Excursion Booking Number:</strong> {order_number} <br/>"
        template += f"<strong>Total:</strong> {item['subTotal']} <hr>"

    template += f"<strong style='background-color:#f85a15; padding: 10px; color:#ffffff;'>Amount Paid:</strong> ${anticipo}<hr>"
    template += f"<strong style='background-color:#f85a15; padding: 10px; color:#ffffff;'>Payment due upon pickup:</strong> ${pay_at_pickup}<hr>"


    email = EmailMultiAlternatives(
        'From Punta Cana Explore',
        template,
        settings.EMAIL_HOST_USER,
        [guest_email, 'puntacanadiscovery@gmail.com', 'qapuntacana@gmail.com']
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


def calculate_final_amount(initial_price, additional_amount, paypal_percentage_fee, paypal_fixed_fee, additional_percentage):
    # Step 1: Add initial price and additional amount
    total_amount = initial_price + additional_amount

    # Step 2: Add PayPal fees
    paypal_fee = total_amount * paypal_percentage_fee + paypal_fixed_fee
    total_amount += paypal_fee

    # Step 3: Add additional percentage
    additional_amount = total_amount * additional_percentage
    total_amount += additional_amount
    
    # Round the total_amount to the nearest integer
    total_amount = Decimal(total_amount).quantize(Decimal('1.'), rounding=ROUND_HALF_UP)

    return total_amount


# def calculate_final_amount(initial_price, additional_amount, paypal_percentage_fee, paypal_fixed_fee, additional_percentage):
#     # Step 1: Add initial price and additional amount
#     total_amount = initial_price + additional_amount

#     # Step 2: Add PayPal fees
#     paypal_fee = total_amount * paypal_percentage_fee + paypal_fixed_fee
#     total_amount += paypal_fee

#     # Step 3: Add additional percentage
#     additional_amount = total_amount * additional_percentage
#     total_amount += additional_amount

#     return total_amount


# initial_price = 71.82
# additional_amount = 15
# paypal_percentage_fee = 0.05
# paypal_fixed_fee = 0.49
# additional_percentage = 0.20  # 20%

# final_amount = calculate_final_amount(initial_price, additional_amount, paypal_percentage_fee, paypal_fixed_fee, additional_percentage)
# print(f'The final amount is: ${final_amount:.2f}')

