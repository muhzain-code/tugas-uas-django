from django.shortcuts import render, get_object_or_404
from zainul.models import Siswa


def daftar(request):
    """Registration form view"""
    return render(request, "hasan/daftar.html")


def sukses(request, pk):
    """Success page after registration"""
    siswa = get_object_or_404(Siswa, pk=pk)
    return render(request, "hasan/sukses.html", {"siswa": siswa})
