import logging
from datetime import datetime
from django.http import HttpResponse HttpRequest
from typing import Callable, Any
from django.http import HttpResponseForbidden


   
class RequestLoggingMiddleware:
    def __init__(self , get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response
        self.logger = logging.getLogger('request_logger')

    def __call__(self, request):
        start_time = datetime.now()
        path = request.path
        user = request.user if request.user.is_authenticated else 'Anonymous'
        logging_message = (f'{datetime.now()} - User:{user} -Path:{request.path}')
    
        response = self.get_response(request)
        return response


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response
        self.allowed_start_time = datetime.strptime('06:00:00', '%H:%M:%S').time()
        self.allowed_end_time = datetime.strptime('09:00:00', '%H:%M:%S').time()

    def __call__(self , request):
        current_time = datetime.now().time()
        if not allowed_start_time <= current_time <= allowed_end_time:
            return.HttpResponseForbidden('Access denied between 6:00 and 9:00')
        # If the request is within the allowed time, proceed to the next middleware or view
        return self.getresponse(request )

class OffensiveLanguageMiddleware:
    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response
        self.message_count = {}
        self.set_limit = 5 
        self.time_window_sleep = 60 

    def __call__(self, request: HttpRequest) -> HttpResponse:
       if request.method == 'POST' and '/api/chats/message' in request.POST:
        ip_address = request.META.get('REMOTE_ADDR')
        if ip_address not in self.message_count:
            self.message_count[ip_address] = 0
        self.message_count[ip_address] = [
            t for t in self.message_count[ip_address] if t > datetime.now().timestamp() - self.time_window_sleep
        ]
        if len(self.message_count[ip_address]) >= self.set_limit:
            return HttpResponse('Too many requests', status=429)

        
        response = self.get_response(request)
        return response




 class RolepermissionMiddleware:
    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response

class RolepermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Example: Only allow staff users to access /admin/ paths
        if request.path.startswith('/admin/'):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("authecation is required ")
        
        # You can add more role checks here

        return self.get_response(request)

