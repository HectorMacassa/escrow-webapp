from django.contrib import admin
from .models import User, Contract, Message, CourierService, ContractCourier

admin.site.register(User)
admin.site.register(Contract)
admin.site.register(Message)
admin.site.register(CourierService)
admin.site.register(ContractCourier)
