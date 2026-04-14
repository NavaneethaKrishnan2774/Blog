from django.shortcuts import redirect
from django.urls import reverse

class RedirectAuthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            paths_to_redirect = [
                reverse('blog:login'),
                reverse('blog:register'),
            ]

            if request.path in paths_to_redirect:
                return redirect('blog:index')

        return self.get_response(request)


class RestrictAuthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            allowed_paths = [
                reverse('blog:login'),
                reverse('blog:register'),
                reverse('blog:forgot_password')
            ]

            if request.path not in allowed_paths:
                return redirect('blog:login')

        return self.get_response(request)