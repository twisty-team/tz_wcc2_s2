from rest_framework import serializers
from .models import Exchange, Picture


class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = ('id', 'toy_to_change', 'owner')

    def create(self, validated_data):
        toy = Exchange(
            toy_to_change=validated_data['toy_to_change'],
            owner=validated_data['owner']
        )
        toy.save()
        return toy

    def partial_update(self, instance):
        exchange = instance
        instance.active = False
        instance.save()
        return instance

class FileSerializer(serializers.Serializer):
    image = serializers.ListField(
        child=serializers.FileField(max_length=100000,
                                    allow_empty_file=False,
                                    use_url=False)
    )

    def create(self, validated_data):
        toy = Exchange.objects.latest('created_at')
        image = validated_data.pop('image')
        for img in image:
            photo = Picture.objects.create(
                image=img, blogs=blogs, **validated_data)
        return photo


class FormDataCreateToy(serializers.Serializer):
    user_name = serializers.CharField(max_length=255)
    contact = serializers.CharField(max_length=14)
    toy_name = serializers.CharField(max_length=255)
    toy_to_change = serializers.CharField(max_length=255)
    pictures = FileSerializer(many=True)

    def create(self, validated_data):
        print(validated_data)
