from django.test import TestCase
from django.contrib.auth.models import User
from unittest.mock import patch
from .models import Review, Business, Alert
from django.urls import reverse

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.business = Business.objects.create(
            name="Test Business",
            email="test@example.com",
            phone_number="1234567890",
            owner=self.user
        )
        self.review = Review.objects.create(business=self.business, rating=1, comment="Bad service", user=self.user)

    def test_review_creation(self):
        self.assertEqual(self.review.rating, 1)
        self.assertEqual(self.review.comment, "Bad service")

class ServiceTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.business = Business.objects.create(
            name="Test Business",
            email="test@example.com",
            phone_number="1234567890",
            owner=self.user
        )
        self.review = Review.objects.create(business=self.business, rating=1, comment="Bad service", user=self.user)

    @patch('reviews.notifications.send_email_alert')
    def test_send_email_alert(self, mock_send_email_alert):
        alert = Alert.objects.create(business=self.business, review=self.review)
        mock_send_email_alert(alert.id)
        mock_send_email_alert.assert_called_once()

    @patch('reviews.notifications.send_sms_alert')
    def test_send_sms_alert(self, mock_send_sms_alert):
        alert = Alert.objects.create(business=self.business, review=self.review)
        mock_send_sms_alert(alert.id)
        mock_send_sms_alert.assert_called_once()

class ViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.business = Business.objects.create(
            name="Test Business",
            email="test@example.com",
            phone_number="1234567890",
            owner=self.user
        )

    def test_create_review_endpoint(self):
        data = {
            "business": self.business.id,
            "rating": 1,
            "comment": "Poor experience",
            "user": self.user.id
        }
        response = self.client.post(reverse('review-list'), data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Alert.objects.filter(business=self.business).exists())
