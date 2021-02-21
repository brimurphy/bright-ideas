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

    def handle_payment_intent_succeeded(self, event):
        # Handle payment_intent.succeeded webhook event
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        # Handle payment_intent.failed webhook event
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)
