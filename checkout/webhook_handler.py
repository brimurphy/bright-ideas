from django.http import HttpResponse


class StripeWH_Handler:
    # Handle Stripe Webhooks

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        # Handle generic webhook event
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)

    # Using Django
    @csrf_exempt
    def my_webhook_view(request):
        payload = request.body
        event = None

        try:
            event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
            )
        except ValueError as e:
            # Invalid payload
            return HttpResponse(status=400)

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
