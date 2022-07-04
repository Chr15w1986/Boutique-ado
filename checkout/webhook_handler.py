from django.http import HttpResponse


class StripeWH_Handler():
    """ Handle stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle an unknown/unexpected/unknown webhook event """
        return HttpResponse(
            context=f'Webhook Received: {event["type"]}'
            status=200)