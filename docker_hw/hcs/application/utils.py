from django.contrib import messages
from django.shortcuts import redirect

from .settings import LOGIN_URL


def login_required(view_func):
    def wrapped(request, *args, **kwargs):
        if request.user.is_anonymous:
            path = request.build_absolute_uri()
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(path, LOGIN_URL)
        else:
            return view_func(request, *args, **kwargs)

    return wrapped


def admin_login_required(view_func):
    def wrapped(request, *args, **kwargs):
        if request.user.is_anonymous:
            path = request.build_absolute_uri()
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(path, '/users/login/')
        else:
            if request.user.is_staff:
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, 'You do not have sufficient rights to do this!')
                return redirect('users')

    return wrapped
