from django.db import models
from django.contrib.auth.models import User
from .services import AlertService

class Business(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)

class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        AlertService.create_alert_for_review(self)

class Alert(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
