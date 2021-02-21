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
    // If the client secret was rendered server-side as a data-secret attribute
    // on the <form> element, you can retrieve it here by calling `form.dataset.secret`
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
        card: card,
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
        card.update({'disabled': false});
        $('#submit-btn').attr('disabled', false);
    
    } else {
        // The payment has been processed!
        if (result.paymentIntent.status === 'succeeded') {
            form.submit();
        }
    }
  });
});