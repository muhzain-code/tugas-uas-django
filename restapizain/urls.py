from django.urls import path
from . import views


urlpatterns = [
    path(
        "api/v1/tahun-akademik/",
        views.tahun_list_create,
        name="tahun_list_create",
    ),
    path(
        "api/v1/tahun-akademik/<int:pk>/",
        views.tahun_detail,
        name="tahun_detail",
    ),
]