from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Alert
from .notifications import send_email_alert, send_sms_alert

@receiver(post_save, sender=Alert)
def handle_alert(sender, instance, **kwargs):
    if not instance.sent:
        instance.sent = True
        instance.save()
