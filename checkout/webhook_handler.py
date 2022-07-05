from django.http import HttpResponse


class StripeWH_Handler():
    """ Handle stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle an unknown/unexpected/unknown webhook event """
        return HttpResponse(
            context=f'Unhandled Webhook Received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handle payment_intent.succeeded webhook from stripe """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            context=f'Webhook Received: {event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        """ Handle payment_intent.payment_failed webhook from stripe """
        return HttpResponse(
            context=f'Webhook Received: {event["type"]}',
            status=200)
