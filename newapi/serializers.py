from rest_framework import serializers

from .models import New

class NewSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = New