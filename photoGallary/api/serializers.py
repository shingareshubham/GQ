from rest_framework import serializers

from photoGallary.models import (
    photo
)


class photoSerializer(serializers.ModelSerializer):
    class Meta:
        model = photo
        fields = '__all__'
