from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from escrow_app.views import (
    UserViewSet, ContractViewSet, MessageViewSet,
    CourierServiceViewSet, ContractCourierViewSet, home
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'contracts', ContractViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'courier_services', CourierServiceViewSet)
router.register(r'contract_couriers', ContractCourierViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', home),
]
