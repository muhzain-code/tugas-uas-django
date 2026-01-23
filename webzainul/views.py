from django.shortcuts import render


def index(request):
    """Landing page view"""
    return render(request, "webzainul/index.html")


def login_page(request):
    """Login page view"""
    return render(request, "webzainul/login.html")


def dashboard_page(request):
    """Dashboard page view for registered students"""
    return render(request, "webzainul/dashboard.html")


def forgot_password_page(request):
    """Forgot password page view"""
    return render(request, "webzainul/forgot_password.html")
