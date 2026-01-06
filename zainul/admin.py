from django.contrib import admin
from .models import (
Negara, Provinsi, KabupatenKota, Kecamatan, DesaKelurahan,
TahunAkademik, Jurusan, Wali,
JenisBerkas, Siswa, Berkas
)

@admin.register(Siswa)
class SiswaAdmin(admin.ModelAdmin):
    list_display = ('nama','nisn','nik')
    search_fields = ('nama', 'nisn')
# ===============================
# MASTER WILAYAH
# ===============================
@admin.register(Negara)
class NegaraAdmin(admin.ModelAdmin):
    list_display = ('nama', 'kode')
    search_fields = ('nama', 'kode')

@admin.register(Provinsi)
class ProvinsiAdmin(admin.ModelAdmin):
    list_display = ('nama', 'kode', 'negara')
    list_filter = ('negara',)
    search_fields = ('nama', 'kode')
@admin.register(KabupatenKota)
class KabupatenKotaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'kode', 'provinsi')
    list_filter = ('provinsi',)
    search_fields = ('nama', 'kode')
@admin.register(Kecamatan)
class KecamatanAdmin(admin.ModelAdmin):
    list_display = ('nama', 'kode', 'kabupaten')
    list_filter = ('kabupaten',)
    search_fields = ('nama', 'kode')
@admin.register(DesaKelurahan)
class DesaKelurahanAdmin(admin.ModelAdmin):
    list_display = ('nama', 'kode', 'kecamatan')
    list_filter = ('kecamatan',)
    search_fields = ('nama', 'kode')

# ===============================
# MASTER AKADEMIK & IDENTITAS
# ===============================
@admin.register(TahunAkademik)
class TahunAkademikAdmin(admin.ModelAdmin):
    list_display = ('nama', 'mulai', 'selesai', 'aktif')
    list_editable = ('aktif',)
    list_filter = ('aktif',)
    search_fields = ('nama',)
    ordering = ('-mulai',)
@admin.register(Jurusan)
class JurusanAdmin(admin.ModelAdmin):
    list_display = ('nama', 'keterangan')
    search_fields = ('nama',)
@admin.register(Wali)
class WaliAdmin(admin.ModelAdmin):
    list_display = ('nama', 'hubungan', 'pekerjaan', 'no_hp')
    search_fields = ('nama', 'no_hp', 'pekerjaan')
    list_filter = ('hubungan',)

# ===============================
# MASTER JENIS BERKAS
# ===============================
@admin.register(JenisBerkas)
class JenisBerkasAdmin(admin.ModelAdmin):
    list_display = ('nama', 'kode', 'wajib', 'aktif', 'urutan')
    list_editable = ('wajib', 'aktif', 'urutan')
    ordering = ('urutan',)
    search_fields = ('nama', 'kode')
    list_filter = ('aktif', 'wajib')

# ===============================
# INLINE UNTUK BERKAS DI SISWA
# ===============================
class BerkasInline(admin.TabularInline):
    model = Berkas
    extra = 0
    fields = ('jenis', 'file', 'keterangan', 'diverifikasi', 'tanggal_upload')
    readonly_fields = ('tanggal_upload',)
    autocomplete_fields = ('jenis',)
    show_change_link = True