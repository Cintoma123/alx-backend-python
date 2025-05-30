from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import MessageViewSet, ConversationViewSet

# Import your viewsets here
# Ensure you have the correct import paths for your viewsets
router = DefaultRouter()
router.register(r'conversations', ConversationViewSet)
router.register(r'messages', MessageViewSet, basename='Conversation')

nested_router = NestedDefaultRouter(
    router, r'conversations', lookup='conversation'
)
nested_router.register(
    r'messages', MessageViewSet, basename='conversation-message'
)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
]