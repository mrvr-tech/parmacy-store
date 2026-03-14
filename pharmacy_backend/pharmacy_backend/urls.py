"""
URL configuration for pharmacy_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
URL configuration for pharmacy_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/settings/
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def home_redirect(request):
    """Redirect to appropriate dashboard based on user role"""
    if request.user.is_authenticated:
        if request.user.role == 'store':
            return redirect('/store/store/dashboard/')
        elif request.user.role == 'lab':
            return redirect('/store/lab/dashboard/')
    return redirect('/store/login/')

urlpatterns = [
    path('', home_redirect, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('store.urls')),
    path('store/', include('store.urls')),
]
