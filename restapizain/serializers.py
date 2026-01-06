from rest_framework import serializers
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


class TahunAkademikSerializer(serializers.ModelSerializer):
    class Meta:
        model = TahunAkademik
        fields = "__all__"

    def validate(self, data):
        mulai = data.get("mulai", getattr(self.instance, "mulai", None))
        selesai = data.get("selesai", getattr(self.instance, "selesai", None))

        if mulai and selesai and selesai <= mulai:
            raise serializers.ValidationError({"selesai": "Harus sesudah 'mulai'."})

        return data


class NegaraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negara
        fields = "__all__"


class ProvinsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provinsi
        fields = "__all__"


class KabupatenKotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = KabupatenKota
        fields = "__all__"


class KecamatanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kecamatan
        fields = "__all__"


class DesaKelurahanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesaKelurahan
        fields = "__all__"


class JurusanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jurusan
        fields = "__all__"


class WaliSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wali
        fields = "__all__"


class JenisBerkasSerializer(serializers.ModelSerializer):
    class Meta:
        model = JenisBerkas
        fields = "__all__"
