from rest_framework import serializers
from user.serializer import UserSerializer
from . import models


class PartSerializer(serializers.ModelSerializer):
    user_added = UserSerializer(read_only=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = models.Part

        fields = '__all__'


class PartLocationFilterSerializer(serializers.Serializer):
    user_lat = serializers.FloatField(required=False)
    user_lon = serializers.FloatField(required=False)
    max_radius = serializers.IntegerField(required=False)
