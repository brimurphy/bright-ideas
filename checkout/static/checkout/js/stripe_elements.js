// 

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);

// Set your publishable key
var stripe = Stripe(stripePublicKey);

// Set up Stripe.js and Elements to use in checkout form
var elements = stripe.elements();
var style = {
  base: {
    color: "#000",
    fontFamily: '"Montserrat", sans-serif',
    fontSize: '1rem'
  },
  invalid: {
      color: '#d01114',
      iconColor: '#d01114'
  }
};

var card = elements.create("card", { style: style });
card.mount("#card-element");

card.addEventListener('change', function(event) {
    var displayError = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon text-red" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span class="small text-red">${event.error.message}</span>`
        ;
        $(displayError).html(html);
    } else {
        displayError.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({'disabled': true});
    $('#submit-btn').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#spinner').fadeToggle(100);
    
    var saveInfo = Boolean($('#save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
            card: card,
            billing_details: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                email: $.trim(form.email.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address1.value),
                    city: $.trim(form.town_or_city.value),
                    state: $.trim(form.county.value),
                    country: $.trim(form.country.value),
                }
            }
        },
        shipping: {
            name: $.trim(form.full_name.value),
            phone: $.trim(form.phone_number.value),
            address: {
                line1: $.trim(form.street_address1.value),
                line2: $.trim(form.street_address1.value),
                city: $.trim(form.town_or_city.value),
                postal_code: $.trim(form.postcode.value),
                state: $.trim(form.county.value),
                country: $.trim(form.country.value),
        }
    }
        }).then(function(result) {
            if (result.error) {
                var displayError = document.getElementById('card-errors');
                var html = `
                    <span class="icon text-red" role="alert">
                        <i class="fas fa-times"></i>
                    </span>
                    <span class="small text-red">${result.error.message}</span>`
                ;
                $(displayError).html(html);
                $('#payment-form').fadeToggle(100);
                $('#spinner').fadeToggle(100);
                card.update({'disabled': false});
                $('#submit-btn').attr('disabled', false);
            
            } else {
                // The payment has been processed!
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function() {
        location.reload();
    });
});
