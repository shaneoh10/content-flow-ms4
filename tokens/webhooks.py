from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from .webhook_handler import StripeWebhookHandler

import stripe

# https://stripe.com/docs/webhooks & Code Institute Boutique Ado project


@require_POST
@csrf_exempt
def webhook(request):
    """Listen for webhooks from Stripe"""
    stripe.api_key = settings.STRIPE_SECRET_KEY
    wh_secret = settings.STRIPE_WH_SECRET

    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, wh_secret)
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Set up webhook handler
    handler = StripeWebhookHandler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        "payment_intent.succeeded": handler.handle_payment_intent_succeeded,
        "payment_intent.payment_failed": handler.handle_payment_intent_payment_failed,
    }

    # Get webhook type from Stripe
    event_type = event["type"]

    # If there's a handler for the event get it from the event map or
    # use the generic handler by default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call event hanler with the event
    response = event_handler(event)
    return response
