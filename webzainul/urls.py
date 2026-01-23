from django.urls import path
from . import views

app_name = "webzainul"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_page, name="login"),
    path("dashboard/", views.dashboard_page, name="dashboard"),
    path("lupa-password/", views.forgot_password_page, name="forgot_password"),
]
