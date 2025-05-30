from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter  
from .views import ConversationViewSet, MessageViewSet  # 

# Import your viewsets here
# Ensure you have the correct import paths for your viewsets
router = DefaultRouter()
router.register(r'Message', MessageViewSet)
router.register(r'Conversation', ConservationViewSet, basename='Conversation')

nested_router = NestedDefaultRouter(
    router, r'Conversation', lookup='conversation'
)
nested_router.register(
    r'Message', MessageViewSet, basename='conversation-message'
)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
]