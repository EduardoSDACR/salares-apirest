from rest_framework.routers import DefaultRouter
from apirest.views import *

router_apirest = DefaultRouter()

# Routes
router_apirest.register(prefix='AppPermArtAditionals', basename='AppPermArtAditionals', viewset=AppPermArtAditionals)
router_apirest.register(prefix='AppPermArtAssociatedEquipments', basename='AppPermArtAssociatedEquipments', viewset=AppPermArtAssociatedEquipments)