from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from zainul.models import TahunAkademik
from .serializers import TahunAkademikSerializer


@api_view(["GET", "POST"])
def tahun_list_create(request):
    if request.method == "GET":
        qs = TahunAkademik.objects.all().order_by("-mulai")
        return Response(TahunAkademikSerializer(qs, many=True).data)

    ser = TahunAkademikSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)

    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def tahun_detail(request, pk):
    obj = get_object_or_404(TahunAkademik, pk=pk)

    if request.method == "GET":
        return Response(TahunAkademikSerializer(obj).data)

    if request.method in ["PUT", "PATCH"]:
        ser = TahunAkademikSerializer(
            obj,
            data=request.data,
            partial=request.method == "PATCH"
        )
        if ser.is_valid():
            ser.save()
            return Response(ser.data)

        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
