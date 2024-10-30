from django.core.mail import send_mail
from twilio.rest import Client
from django.conf import settings
import json
import logging
from celery import shared_task

logger = logging.getLogger(__name__)

def get_twilio_client():
    return Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

@shared_task
def send_email_alert(alert_id):
    from .models import Alert
    alert = Alert.objects.get(id=alert_id)
    subject = f"Low Rating Alert for {alert.business.name}"
    message = f"New low rating:\nRating: {alert.review.rating}\nComment: {alert.review.comment}"
    try:
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [alert.business.email])
        logger.info((f"Email alert sent to {alert.business.email} for review {alert.review.id}"))
    except Exception as e:
        logger.error(f"Failed to send email alert for review {alert.review.id}: {e}")

@shared_task
def send_sms_alert(alert_id):
    from .models import Alert
    client = get_twilio_client()
    alert = Alert.objects.get(id=alert_id)
    content_variables = json.dumps({
        '1': alert.business.name,
        '2': str(alert.review.rating),
        '3': alert.review.comment
    })
    if alert.business.phone_number:
        try:
            client.messages.create(
                content_sid=f'{settings.TWILIO_TEMPLATE_SID}',
                from_=f'whatsapp:{settings.TWILIO_PHONE_NUMBER}',
                to=f'whatsapp:{alert.business.phone_number}',
                content_variables=content_variables
            )
            logger.info((f"Whatsapp alert sent to {alert.business.phone_number} for review {alert.review.id}"))
        except Exception as e:
            logger.error(f"Error sending WhatsApp message: {e}")
        