from rest_framework import serializers
from .models import MagicNumber


class MagicNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagicNumber
        fields = ['number']
