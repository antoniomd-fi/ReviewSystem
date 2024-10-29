from .notifications import send_email_alert, send_sms_alert
import logging

logger = logging.getLogger(__name__)

class AlertService:
    @staticmethod
    def create_alert_for_review(review):
        from .models import Alert
        if review.rating <= 2:
            alert, created = Alert.objects.get_or_create(
                business=review.business, 
                review=review,
                defaults={'sent': False}
            )
            if(created or not alert.sent):
                logger.info(f"Creating alert for {review.business.name} due to low rating.")
                AlertService.notify(alert)

    @staticmethod
    def notify(alert):
        try:
            send_email_alert.delay(alert.id)
            send_sms_alert.delay(alert.id)
            alert.sent = True
            alert.save()
            logger.info(f"Alert marked as sent for review {alert.review.id}.")
        except Exception as e:
            logger.error(f"Failed to send notifications for alert {alert.id}: {e}")
