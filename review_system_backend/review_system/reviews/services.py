from .models import Alert
from .notifications import send_email_alert, send_sms_alert

class AlertService:
    @staticmethod
    def create_alert_for_review(review):
        if review.rating <= 2:
            alert = Alert.objects.create(business=review.business, review=review)
            AlertService.notify(alert)

    @staticmethod
    def notify(alert):
        send_email_alert(alert)
        send_sms_alert(alert)
