from rest_framework import serializers
from .models import StoreStatus, BusinessHours, Timezones

class StoreStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreStatus
        fields = '__all__'

class BusinessHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessHours
        fields = '__all__'

class TimezonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timezones
        fields = '__all__'