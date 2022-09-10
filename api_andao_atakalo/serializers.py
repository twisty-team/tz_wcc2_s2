from rest_framework import serializers
from .models import Toy


class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = '__all__'