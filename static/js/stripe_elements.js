
var stripe_public_key = document.getElementById('id_stripe_public_key').text.slice(1,-1);
var client_secret = document.getElementById('id_client_secret').text.slice(1,-1)
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function(event){
    var errorDive = document.getElementById('card-errors')
    if(event.error){
        var html = `
        <span class="icon" role="alert>
        <i class="fa-solid fa-x">
        </span>
        <span></i> ${event.error.message}</span>
        `
        $(errorDive).html(html)
    }else{
        errorDive.textContent = ''
    }
});


// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(client_secret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});