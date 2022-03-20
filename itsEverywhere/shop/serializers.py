from rest_framework import serializers
from .models import Registration, Order

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

class PlaceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['order_id']
        # fields = '__all__'