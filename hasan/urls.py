from django.urls import path
from . import views

app_name = "hasan"
urlpatterns = [
    path("daftar/", views.daftar, name="daftar"),
    path("sukses/<int:pk>/", views.sukses, name="sukses"),
]
