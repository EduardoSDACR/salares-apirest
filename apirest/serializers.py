from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apirest.models import *

class AppPermArtAditionalsSerializer(ModelSerializer):
    class Meta:
        model=AppPermArtAditionals
        fields='__all__'

class AppPermArtAssociatedEquipmentsSerializer(ModelSerializer):
    class Meta:
        model=AppPermArtAssociatedEquipments
        fields='__all__'