from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def store_keeper_required(view_func):
    """Decorator to ensure only Store Keepers can access the view"""
    @wraps(view_func)
    @login_required(login_url='login')
    def wrapper(request, *args, **kwargs):
        if request.user.role != 'store':
            return redirect('lab_dashboard')
        return view_func(request, *args, **kwargs)
    return wrapper


def lab_user_required(view_func):
    """Decorator to ensure only Lab Users can access the view"""
    @wraps(view_func)
    @login_required(login_url='login')
    def wrapper(request, *args, **kwargs):
        if request.user.role != 'lab':
            return redirect('store_dashboard')
        return view_func(request, *args, **kwargs)
    return wrapper


def authenticated_required(view_func):
    """Simple authentication decorator"""
    @wraps(view_func)
    @login_required(login_url='login')
    def wrapper(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
    return wrapper
