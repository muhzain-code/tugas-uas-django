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
    Siswa,
    Berkas,
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

class BerkasSerializer(serializers.ModelSerializer):
    jenis = JenisBerkasSerializer(read_only=True)
    jenis_id = serializers.PrimaryKeyRelatedField(
        source="jenis", queryset=JenisBerkas.objects.all(), write_only=True
    )
    siswa_id = serializers.PrimaryKeyRelatedField(
        source="siswa", queryset=Siswa.objects.all(), write_only=True, required=False
    )

    class Meta:
        model = Berkas
        fields = [
            "id",
            "siswa",
            "siswa_id",
            "jenis",
            "jenis_id",
            "file",
            "keterangan",
            "tanggal_upload",
            "diverifikasi",
        ]
        read_only_fields = ["tanggal_upload"]
        extra_kwargs = {
            "siswa": {"read_only": True},
        }


class SiswaSerializer(serializers.ModelSerializer):
    alamat_lengkap = serializers.ReadOnlyField()

    negara = NegaraSerializer(read_only=True)
    provinsi = ProvinsiSerializer(read_only=True)
    kabupaten = KabupatenKotaSerializer(read_only=True)
    kecamatan = KecamatanSerializer(read_only=True)
    desa = DesaKelurahanSerializer(read_only=True)
    tahun_akademik = TahunAkademikSerializer(read_only=True)
    jurusan = JurusanSerializer(read_only=True)
    wali = WaliSerializer(read_only=True)

    berkas = BerkasSerializer(many=True, read_only=True)

    negara_id = serializers.PrimaryKeyRelatedField(
        source="negara", queryset=Negara.objects.all(), write_only=True, required=False
    )
    provinsi_id = serializers.PrimaryKeyRelatedField(
        source="provinsi",
        queryset=Provinsi.objects.all(),
        write_only=True,
        required=False,
    )
    kabupaten_id = serializers.PrimaryKeyRelatedField(
        source="kabupaten",
        queryset=KabupatenKota.objects.all(),
        write_only=True,
        required=False,
    )
    kecamatan_id = serializers.PrimaryKeyRelatedField(
        source="kecamatan",
        queryset=Kecamatan.objects.all(),
        write_only=True,
        required=False,
    )
    desa_id = serializers.PrimaryKeyRelatedField(
        source="desa",
        queryset=DesaKelurahan.objects.all(),
        write_only=True,
        required=False,
    )
    tahun_akademik_id = serializers.PrimaryKeyRelatedField(
        source="tahun_akademik",
        queryset=TahunAkademik.objects.all(),
        write_only=True,
        required=False,
    )
    jurusan_id = serializers.PrimaryKeyRelatedField(
        source="jurusan",
        queryset=Jurusan.objects.all(),
        write_only=True,
        required=False,
    )
    wali_id = serializers.PrimaryKeyRelatedField(
        source="wali", queryset=Wali.objects.all(), write_only=True, required=False
    )

    class Meta:
        model = Siswa
        fields = [
            "id",
            "nama",
            "nisn",
            "email",
            "tanggal_daftar",
            "foto",
            "tahun_akademik",
            "tahun_akademik_id",
            "jurusan",
            "jurusan_id",
            "nik",
            "tempat_lahir",
            "tanggal_lahir",
            "jenis_kelamin",
            "agama",
            "wali",
            "wali_id",
            "status_pendaftaran",
            "negara",
            "negara_id",
            "provinsi",
            "provinsi_id",
            "kabupaten",
            "kabupaten_id",
            "kecamatan",
            "kecamatan_id",
            "desa",
            "desa_id",
            "alamat_detail",
            "alamat_lengkap",
            "berkas",
        ]
        read_only_fields = ["alamat_lengkap", "tanggal_daftar"]

    def validate(self, data):
        negara = data.get("negara") or getattr(self.instance, "negara", None)
        provinsi = data.get("provinsi") or getattr(self.instance, "provinsi", None)

        if provinsi and negara and provinsi.negara_id != negara.id:
            raise serializers.ValidationError(
                "Provinsi tidak sesuai dengan negara yang dipilih."
            )
        return data
