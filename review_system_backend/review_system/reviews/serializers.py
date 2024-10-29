from rest_framework import serializers, viewsets
from .models import Business, Review

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("The raiting must be between 1 and 5")
        return value

    def validate(self, data):
        if not data.get("business") or not data.get("user"):
            raise serializers.ValidationError("Business and User are required.")
        return data
