from rest_framework import serializers
from core.models import NadiaProfile


class NadiaProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = NadiaProfile
        fields = ['app_installed', 'app_downloaded']