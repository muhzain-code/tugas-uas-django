from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TahunViewSet,
    NegaraViewSet,
    ProvinsiViewSet,
    KabupatenKotaViewSet,
    KecamatanViewSet,
    DesaKelurahanViewSet,
    JurusanViewSet,
    WaliViewSet,
    JenisBerkasViewSet,
    LogoutTokenView,
    LogoutJWTView,

)
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r"tahun", TahunViewSet, basename="tahun")
router.register(r"negara", NegaraViewSet, basename="negara")
router.register(r"provinsi", ProvinsiViewSet, basename="provinsi")
router.register(r"kabupaten-kota", KabupatenKotaViewSet, basename="kabupaten-kota")
router.register(r"kecamatan", KecamatanViewSet, basename="kecamatan")
router.register(r"desa-kelurahan", DesaKelurahanViewSet, basename="desa-kelurahan")
router.register(r"jurusan", JurusanViewSet, basename="jurusan")
router.register(r"wali", WaliViewSet, basename="wali")
router.register(r"jenis-berkas", JenisBerkasViewSet, basename="jenis-berkas")

urlpatterns = [
    path("", include(router.urls)),
    path("token-auth/", obtain_auth_token, name="api_token_auth"),
    path("token-auth/logout/", LogoutTokenView.as_view(), name="api_token_logout"),
    path("jwt/token/", TokenObtainPairView.as_view(), name="jwt_obtain_pair"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    path("jwt/logout/", LogoutJWTView.as_view(), name="jwt_logout"),
]
