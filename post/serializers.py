from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=30)
    slug = serializers.SlugField(required=False)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance
