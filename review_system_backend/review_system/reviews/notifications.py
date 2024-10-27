from django.core.mail import send_mail
from twilio.rest import Client
from django.conf import settings

def send_email_alert(alert):
    subject = f"Low Rating Alert for {alert.business.name}"
    message = f"New low rating:\nRating: {alert.review.rating}\nComment: {alert.review.comment}"
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [alert.business.email])

def send_sms_alert(alert):
    if alert.business.phone_number:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = f"Low rating alert for {alert.business.name}: Rating {alert.review.rating}\n{alert.review.comment}"
        client.messages.create(
            body=message,
            from_=f'whatsapp:{settings.TWILIO_PHONE_NUMBER}',
            to=f'whatsapp:{alert.business.phone_number}'
        )
        