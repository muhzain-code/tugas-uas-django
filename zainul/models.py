from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.conf import settings


# ===============================
# MASTER WILAYAH
# ===============================
class Negara(models.Model):
    kode = models.CharField(
        max_length=3,
        unique=True,
        help_text="Kode ISO-3166-1 alpha-3 (misal: IDN)",
    )
    nama = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Negara"
        ordering = ["nama"]

    def __str__(self):
        return self.nama


class Provinsi(models.Model):
    negara = models.ForeignKey(
        Negara,
        on_delete=models.CASCADE,
        related_name="provinsi",
    )
    kode = models.CharField(max_length=10)
    nama = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Provinsi"
        unique_together = [("negara", "nama")]
        ordering = ["nama"]

    def __str__(self):
        return self.nama


class KabupatenKota(models.Model):
    provinsi = models.ForeignKey(
        Provinsi,
        on_delete=models.CASCADE,
        related_name="kabupaten",
    )
    kode = models.CharField(max_length=10)
    nama = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "Kabupaten Kota"
        unique_together = [("provinsi", "nama")]
        ordering = ["nama"]

    def __str__(self):
        return self.nama


class Kecamatan(models.Model):
    kabupaten = models.ForeignKey(
        KabupatenKota,
        on_delete=models.CASCADE,
        related_name="kecamatan",
    )
    kode = models.CharField(max_length=10)
    nama = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "Kecamatan"
        unique_together = [("kabupaten", "nama")]
        ordering = ["nama"]

    def __str__(self):
        return self.nama


class DesaKelurahan(models.Model):
    kecamatan = models.ForeignKey(
        Kecamatan,
        on_delete=models.CASCADE,
        related_name="desa",
    )
    kode = models.CharField(max_length=10)
    nama = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "Desa Kelurahan"
        unique_together = [("kecamatan", "nama")]
        ordering = ["nama"]

    def __str__(self):
        return self.nama


# ===============================
# MASTER AKADEMIK & IDENTITAS
# ===============================
class TahunAkademik(models.Model):
    nama = models.CharField(max_length=20, unique=True)  # ex: "2025/2026"
    mulai = models.DateField()
    selesai = models.DateField()
    aktif = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Tahun Akademik"
        ordering = ["-mulai"]

    def __str__(self):
        return self.nama


class Jurusan(models.Model):
    nama = models.CharField(max_length=100, unique=True)
    keterangan = models.TextField(blank=True, null=True)
    aktif = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Jurusan"

    def __str__(self):
        return self.nama


class Wali(models.Model):
    nama = models.CharField(max_length=120)
    hubungan = models.CharField(
        max_length=50,
        help_text="Hubungan: Ayah/Ibu/Wali",
    )
    pekerjaan = models.CharField(max_length=100, blank=True, null=True)
    no_hp = models.CharField(max_length=20, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Wali"

    def __str__(self):
        return f"{self.nama} ({self.hubungan})"


# ===============================
# MASTER JENIS BERKAS
# ===============================
class JenisBerkas(models.Model):
    kode = models.SlugField(max_length=30, unique=True)  # contoh: "kk", "ktp", "raport"
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True, null=True)
    wajib = models.BooleanField(default=True)
    aktif = models.BooleanField(default=True)
    urutan = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name_plural = "Jenis Berkas"
        ordering = ["urutan", "nama"]

    def __str__(self):
        return self.nama


# ===============================
# ENTITAS UTAMA SISWA
# ===============================
class Siswa(models.Model):
    STATUS_AGAMA = [
        ("Islam", "Islam"),
        ("Kristen", "Kristen"),
        ("Hindu", "Hindu"),
        ("Budha", "Budha"),
        ("Kongucu", "Kongucu"),
    ]

    nama = models.CharField(max_length=120)
    nisn = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True, null=True)
    tanggal_daftar = models.DateField(default=timezone.localdate)
    foto = models.ImageField(upload_to="gambar/foto", blank=True)

    tahun_akademik = models.ForeignKey(
        TahunAkademik,
        on_delete=models.PROTECT,
        related_name="siswa",
    )
    jurusan = models.ForeignKey(
        Jurusan,
        on_delete=models.PROTECT,
        related_name="siswa",
    )

    nik = models.CharField(max_length=20, unique=True)
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(
        max_length=1,
        choices=[("L", "Laki-laki"), ("P", "Perempuan")],
    )
    agama = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=STATUS_AGAMA,
    )
    wali = models.ForeignKey(
        Wali,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="anak",
    )

    STATUS_CHOICES = [
        ("DAFTAR", "Terdaftar"),
        ("VERIFIKASI", "Terverifikasi"),
        ("DITOLAK", "Ditolak"),
    ]

    status_pendaftaran = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="DAFTAR",
    )

    # User account for login
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="siswa",
        help_text="Akun login untuk pendaftar",
    )

    # Alamat bertingkat
    negara = models.ForeignKey(
        Negara,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="siswa",
    )
    provinsi = models.ForeignKey(
        Provinsi,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="siswa",
    )
    kabupaten = models.ForeignKey(
        KabupatenKota,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="siswa",
    )
    kecamatan = models.ForeignKey(
        Kecamatan,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="siswa",
    )
    desa = models.ForeignKey(
        DesaKelurahan,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="siswa",
    )
    alamat_detail = models.CharField(
        max_length=255,
        blank=True,
        help_text="Nama jalan, RT/RW, nomor rumah, dll.",
    )

    class Meta:
        verbose_name_plural = "Siswa"
        ordering = ["nama"]
        indexes = [
            models.Index(
                fields=["negara", "provinsi", "kabupaten", "kecamatan", "desa"],
            ),
        ]

    def __str__(self):
        return f"{self.nama} ({self.nisn})"

    def clean(self):
        if self.provinsi and self.negara and self.provinsi.negara_id != self.negara_id:
            raise ValidationError("Provinsi tidak sesuai dengan negara yang dipilih.")
        if (
            self.kabupaten
            and self.provinsi
            and self.kabupaten.provinsi_id != self.provinsi_id
        ):
            raise ValidationError(
                "Kabupaten tidak sesuai dengan provinsi yang dipilih."
            )
        if (
            self.kecamatan
            and self.kabupaten
            and self.kecamatan.kabupaten_id != self.kabupaten_id
        ):
            raise ValidationError(
                "Kecamatan tidak sesuai dengan kabupaten yang dipilih."
            )
        if self.desa and self.kecamatan and self.desa.kecamatan_id != self.kecamatan_id:
            raise ValidationError("Desa tidak sesuai dengan kecamatan yang dipilih.")

    @property
    def alamat_lengkap(self):
        parts = [
            self.alamat_detail,
            getattr(self.desa, "nama", None),
            getattr(self.kecamatan, "nama", None),
            getattr(self.kabupaten, "nama", None),
            getattr(self.provinsi, "nama", None),
            getattr(self.negara, "nama", None),
        ]
        return ", ".join([p for p in parts if p])


# ===============================
# BERKAS PENDAFTARAN
# ===============================
class Berkas(models.Model):
    siswa = models.ForeignKey(
        Siswa,
        on_delete=models.CASCADE,
        related_name="berkas",
    )
    jenis = models.ForeignKey(
        JenisBerkas,
        on_delete=models.PROTECT,
        related_name="unggahan",
    )
    file = models.FileField(upload_to="berkas_siswa/")
    keterangan = models.TextField(blank=True, null=True)
    tanggal_upload = models.DateTimeField(auto_now_add=True)
    diverifikasi = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Berkas"
        ordering = ["-tanggal_upload"]
        constraints = [
            models.UniqueConstraint(
                fields=["siswa", "jenis"],
                name="uniq_berkas_per_siswa_jenis",
            ),
        ]

    def clean(self):
        if (
            Berkas.objects.exclude(pk=self.pk)
            .filter(
                siswa=self.siswa,
                jenis=self.jenis,
            )
            .exists()
        ):
            raise ValidationError(
                "Jenis berkas ini sudah diunggah oleh siswa yang sama."
            )

    def __str__(self):
        return f"{self.siswa.nama} - {self.jenis.nama}"
