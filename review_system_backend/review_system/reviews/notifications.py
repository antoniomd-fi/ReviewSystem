from django.core.mail import send_mail
from twilio.rest import Client
from django.conf import settings
import json

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

def send_email_alert(alert):
    subject = f"Low Rating Alert for {alert.business.name}"
    message = f"New low rating:\nRating: {alert.review.rating}\nComment: {alert.review.comment}"
    try:
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [alert.business.email])
        print((f"Email alert sent to {alert.business.email} for review {alert.review.id}"))
    except Exception as e:
        print(f"Failed to send email alert for review {alert.review.id}: {e}")

def send_sms_alert(alert):
    message_template = 'review_system_template_2'
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
            print((f"Whatsapp alert sent to {alert.business.phone_number} for review {alert.review.id}"))
        except Exception as e:
            print(f"Error sending WhatsApp message: {e}")
        