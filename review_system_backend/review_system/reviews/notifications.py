from django.core.mail import send_mail
from twilio.rest import Client
from django.conf import settings

def send_email_alert(alert):
    subject = f"Low Rating Alert for {alert.business.name}"
    message = f"New low rating:\nRating: {alert.review.rating}\nComment: {alert.review.comment}"
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [alert.business.email])
