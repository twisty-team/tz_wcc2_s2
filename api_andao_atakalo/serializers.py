from rest_framework import serializers
from .models import Exchange, Picture, Owner


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        exclude = ('exchange', 'id')


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        exclude = ('token', 'id')


class ExchangeSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True, read_only=True, required=False)
    owner = OwnerSerializer()

    class Meta:
        model = Exchange
        fields = '__all__'


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


class FormDataCreateExchange(serializers.Serializer):
    user_name = serializers.CharField(max_length=255)
    contact = serializers.CharField(max_length=14)
    toy_name = serializers.CharField(max_length=255)
    toy_to_change = serializers.CharField(max_length=255)
    pictures = serializers.ImageField(max_length=100000)

    def create(self, validated_data):
        print(validated_data)
        return validated_data
