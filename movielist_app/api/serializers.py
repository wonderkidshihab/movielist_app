from rest_framework import serializers
from movielist_app.models import Content, Platform, Review
from rest_framework import generics


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('__all__')


class ContentSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True)

    class Meta:
        model = Content
        fields = ('__all__')


class PlatformSerializer(serializers.ModelSerializer):
    contents = serializers.StringRelatedField(many=True)

    class Meta:
        model = Platform
        fields = ('__all__')
