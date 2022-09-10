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


class FormDataCreateToy(serializers.Serializer):
    user_name = serializers.CharField(max_length=255)
    contact = serializers.CharField(max_length=14)
    toy_name = serializers.CharField(max_length=255)
    toy_to_change = serializers.CharField(max_length=255)
    pictures = serializers.FileField()

    def create(self, validated_data):
        print(validated_data)