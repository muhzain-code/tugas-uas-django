from django.urls import path
from . import views

app_name = "webzainul"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_page, name="login"),
]
