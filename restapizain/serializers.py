from rest_framework import serializers
from zainul.models import TahunAkademik


class TahunAkademikSerializer(serializers.ModelSerializer):
    class Meta:
        model = TahunAkademik
        fields = "__all__"

    def validate(self, data):
        mulai = data.get("mulai", getattr(self.instance, "mulai", None))
        selesai = data.get("selesai", getattr(self.instance, "selesai", None))

        if mulai and selesai and selesai <= mulai:
            raise serializers.ValidationError(
                {"selesai": "Harus sesudah 'mulai'."}
            )

        return data
