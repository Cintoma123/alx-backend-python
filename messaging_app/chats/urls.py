from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConservationViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'Message',MessageViewSet)
router.register(r'Conversation',ConservationViewSet)

urlpatterns = [
    path('',include(router.urls))
]