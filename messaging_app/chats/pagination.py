from rest_framework.pagination import PageNumberPagination
class MessagePagination(PageNumberPagination):
    page_size = 20  # 20 messages per page