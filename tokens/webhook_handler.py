from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# https://stripe.com/docs/webhooks & Code Institute Boutique Ado project


class StripeWebhookHandler():
    """ Class for handling stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle webhook event """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle payment_intent.payment_succeeded webhook
        """
        intent = event.data.object
        username = intent.metadata.username
        tokens = int(intent.metadata.tokens)
        user = get_object_or_404(User, username=username)

        user.userprofile.tokens_balance += tokens
        user.userprofile.save()

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle payment_intent.payment_failed webhook
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
