from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
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
    Siswa,
    Berkas,
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
    SiswaSerializer,
    BerkasSerializer,
)
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView


class TahunViewSet(ModelViewSet):
    queryset = TahunAkademik.objects.all()
    serializer_class = TahunAkademikSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAuthenticated()]


class NegaraViewSet(ModelViewSet):
    queryset = Negara.objects.all()
    serializer_class = NegaraSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAuthenticated()]


class ProvinsiViewSet(ModelViewSet):
    serializer_class = ProvinsiSerializer
    queryset = Provinsi.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        negara_id = self.request.query_params.get("negara")
        if negara_id:
            qs = qs.filter(negara_id=negara_id)
        return qs

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAuthenticated()]


class KabupatenKotaViewSet(ModelViewSet):
    serializer_class = KabupatenKotaSerializer
    queryset = KabupatenKota.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        provinsi_id = self.request.query_params.get("provinsi")
        if provinsi_id:
            qs = qs.filter(provinsi_id=provinsi_id)
        return qs

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAuthenticated()]


class KecamatanViewSet(ModelViewSet):
    serializer_class = KecamatanSerializer
    queryset = Kecamatan.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        kabupaten_id = self.request.query_params.get("kabupaten")
        if kabupaten_id:
            qs = qs.filter(kabupaten_id=kabupaten_id)
        return qs

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAuthenticated()]


class DesaKelurahanViewSet(ModelViewSet):
    serializer_class = DesaKelurahanSerializer
    queryset = DesaKelurahan.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        kecamatan_id = self.request.query_params.get("kecamatan")
        if kecamatan_id:
            qs = qs.filter(kecamatan_id=kecamatan_id)
        return qs

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAuthenticated()]


class JurusanViewSet(ModelViewSet):
    queryset = Jurusan.objects.filter(aktif=True)
    serializer_class = JurusanSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAuthenticated()]


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


class SiswaViewSet(ModelViewSet):
    queryset = Siswa.objects.all().select_related(
        "tahun_akademik",
        "jurusan",
        "wali",
        "negara",
        "provinsi",
        "kabupaten",
        "kecamatan",
        "desa",
    )
    serializer_class = SiswaSerializer
    parser_classes = [JSONParser, FormParser, MultiPartParser]

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated()]


class BerkasViewSet(ModelViewSet):
    queryset = Berkas.objects.all().select_related("siswa", "jenis")
    serializer_class = BerkasSerializer
