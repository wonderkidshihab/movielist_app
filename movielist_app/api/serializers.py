from rest_framework import serializers
from movielist_app.models import Content, Platform


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('__all__')


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ('__all__')
