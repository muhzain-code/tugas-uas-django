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
