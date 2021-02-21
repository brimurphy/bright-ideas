import json
import stripe
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from checkout.webhook_handler import StripeWH_Handler

# Setup
stripe_api_key = settings.STRIPE_SECRET_KEY
wh_secret = settings.STRIPE_WH_SECRET


# Using Django
@csrf_exempt
def webhooks(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
                json.loads(payload), stripe_api_key,
                wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(content=e, status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    return HttpResponse(status=200)

    #  Set up a webhook handler
    handler = StripeWH_Handler(request)

    # Map webhook events relevant handler
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.failed': handler.handle_payment_intent_failed,
    }

    # Get webhook type from Stripe
    event_type = event['type']

    # If there is a handler get it from the event map
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call event handler with the event
    response = event_handler(event)
    return response

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        # contains a stripe.PaymentIntent
        payment_intent = event.data.object
        print('PaymentIntent was successful!')
    elif event.type == 'payment_method.attached':
        # contains a stripe.PaymentMethod
        payment_method = event.data.object 
        print('PaymentMethod was attached to a Customer!')
    # ... handle other event types
    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)
