from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)
    kyc_documents = models.JSONField(blank=True, null=True)
    is_company = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='escrow_app_user_set',  # Avoid clash with auth.User.groups
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='escrow_app_user_set',  # Avoid clash with auth.User.user_permissions
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_query_name='user',
    )

    def __str__(self):
        return self.full_name


class Contract(models.Model):
    STATUS_CHOICES = [
        ('Awaiting Payment', 'Awaiting Payment'),
        ('Awaiting Delivery', 'Awaiting Delivery'),
        ('Complete', 'Complete')
    ]

    buyer = models.ForeignKey(User, related_name='buyer_contracts', on_delete=models.CASCADE)
    seller = models.ForeignKey(User, related_name='seller_contracts', on_delete=models.CASCADE)
    item_details = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Awaiting Payment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Contract {self.id} - {self.status}"

class Message(models.Model):
    contract = models.ForeignKey(Contract, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.id} from {self.sender} to {self.recipient}"

class CourierService(models.Model):
    service_name = models.CharField(max_length=255)
    contact_information = models.TextField()

    def __str__(self):
        return self.service_name

class ContractCourier(models.Model):
    contract = models.ForeignKey(Contract, related_name='courier', on_delete=models.CASCADE)
    courier_service = models.ForeignKey(CourierService, related_name='contracts', on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=255, blank=True, null=True)
    pickup_date = models.DateTimeField(blank=True, null=True)
    delivery_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"ContractCourier {self.id} for Contract {self.contract.id}"
