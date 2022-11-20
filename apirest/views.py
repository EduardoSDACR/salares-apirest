from apirest.models import *
from apirest.serializers import *
from rest_framework.viewsets import ModelViewSet

class AppPermArtAditionals(ModelViewSet):    
    serializer_class = AppPermArtAditionalsSerializer
    queryset = AppPermArtAditionals.objects.all()

class AppPermArtAssociatedEquipments(ModelViewSet):
    serializer_class = AppPermArtAssociatedEquipmentsSerializer
    queryset = AppPermArtAssociatedEquipments.objects.all()