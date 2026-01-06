from rest_framework.viewsets import ModelViewSet
from zainul.models import (
    TahunAkademik,
    Negara,
    Provinsi,
    KabupatenKota,
    Kecamatan,
    DesaKelurahan,
    Jurusan,
    Wali,
    JenisBerkas,
)
from .serializers import (
    TahunAkademikSerializer,
    NegaraSerializer,
    ProvinsiSerializer,
    KabupatenKotaSerializer,
    KecamatanSerializer,
    DesaKelurahanSerializer,
    JurusanSerializer,
    WaliSerializer,
    JenisBerkasSerializer,
)
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

class TahunViewSet(ModelViewSet):
    queryset = TahunAkademik.objects.all()
    serializer_class = TahunAkademikSerializer

class NegaraViewSet(ModelViewSet):
    queryset = Negara.objects.all()
    serializer_class = NegaraSerializer

class ProvinsiViewSet(ModelViewSet):
    queryset = Provinsi.objects.all()
    serializer_class = ProvinsiSerializer

class KabupatenKotaViewSet(ModelViewSet):
    queryset = KabupatenKota.objects.all()
    serializer_class = KabupatenKotaSerializer

class KecamatanViewSet(ModelViewSet):
    queryset = Kecamatan.objects.all()
    serializer_class = KecamatanSerializer

class DesaKelurahanViewSet(ModelViewSet):
    queryset = DesaKelurahan.objects.all()
    serializer_class = DesaKelurahanSerializer

class JurusanViewSet(ModelViewSet):
    queryset = Jurusan.objects.all()
    serializer_class = JurusanSerializer

class WaliViewSet(ModelViewSet):
    queryset = Wali.objects.all()
    serializer_class = WaliSerializer

class JenisBerkasViewSet(ModelViewSet):
    queryset = JenisBerkas.objects.all()
    serializer_class = JenisBerkasSerializer

class LogoutTokenView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response(
            {"detail": "Token dihapus (logout)."},
            status=status.HTTP_200_OK,
        )

class LogoutJWTView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh", None)
        if not refresh_token:
            return Response(
                {"detail": "Refresh token tidak ditemukan di body."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"detail": "Refresh token di-blacklist."},
                status=status.HTTP_205_RESET_CONTENT,
            )
        except Exception:
            return Response(
                {"detail": "Refresh token tidak valid atau sudah di-blacklist."},
                status=status.HTTP_400_BAD_REQUEST,
            )

