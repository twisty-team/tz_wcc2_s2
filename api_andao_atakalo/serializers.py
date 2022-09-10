from rest_framework import serializers
from .models import Toy


class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = ('name', 'toy_to_change', 'owner', 'token')

    def create(self, validated_data):
        toy = Toy(name=validated_data['name'],
                  toy_to_change=validated_data['toy_to_change'],
                  owner=validated_data['owner'])
        toy.save()
        return toy
