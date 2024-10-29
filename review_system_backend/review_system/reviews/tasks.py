from celery import shared_task
from .notifications import send_email_alert, send_sms_alert
from .models import Alert

@shared_task
def send_email_alert_task(alert_id):
    alert = Alert.objects.get(id=alert_id)
    send_email_alert(alert)

@shared_task
def send_sms_alert_task(alert_id):
    alert = Alert.objects.get(id=alert_id)
    send_sms_alert(alert)
