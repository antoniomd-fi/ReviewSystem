from django.test import TestCase
from django.core import mail
from .models import Business, Review, Alert
from .notifications import send_email_alert, send_whatsapp_alert

class NotificationTests(TestCase):
    def setUp(self):
        self.business = Business.objects.create(
            name="Testing Bussiness", owner_id=1, email="ownero@example.com", phone_number="+123456789"
        )
        self.review = Review.objects.create(business=self.business, user_id=1, rating=1, comment="Very Bad")

    def test_send_email_alert(self):
        alert = Alert.objects.create(business=self.business, review=self.review)
        send_email_alert(alert)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("Low Rating Alert", mail.outbox[0].subject)

     def test_send_whatsapp_alert(self):
        alert = Alert.objects.create(business=self.business, review=self.review)
        send_whatsapp_alert(alert)
