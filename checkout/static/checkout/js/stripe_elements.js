// 

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);

// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/account/apikeys
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