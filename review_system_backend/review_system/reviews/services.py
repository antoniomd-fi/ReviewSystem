from .notifications import send_email_alert, send_sms_alert

class AlertService:
    @staticmethod
    def create_alert_for_review(review):
        from .models import Alert
        if review.rating <= 2:
            alert = Alert.objects.create(business=review.business, review=review)
            AlertService.notify(alert)

    @staticmethod
    def notify(alert):
        try:
            send_email_alert(alert)
        except Exception as e:
            print.error(f"Failed to send email alert: {e}")

        try:
            send_sms_alert(alert)
        except Exception as e:
            print.error(f"Failed to send SMS alert: {e}")
