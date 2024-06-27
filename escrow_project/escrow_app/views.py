from rest_framework import viewsets
from .models import User, Contract, Message, CourierService, ContractCourier
from .serializers import (
    UserSerializer, ContractSerializer, MessageSerializer,
    CourierServiceSerializer, ContractCourierSerializer
)
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class CourierServiceViewSet(viewsets.ModelViewSet):
    queryset = CourierService.objects.all()
    serializer_class = CourierServiceSerializer

class ContractCourierViewSet(viewsets.ModelViewSet):
    queryset = ContractCourier.objects.all()
    serializer_class = ContractCourierSerializer
