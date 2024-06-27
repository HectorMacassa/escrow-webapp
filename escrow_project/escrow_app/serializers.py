from rest_framework import serializers
from .models import User, Contract, Message, CourierService, ContractCourier

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class CourierServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourierService
        fields = '__all__'

class ContractCourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractCourier
        fields = '__all__'
