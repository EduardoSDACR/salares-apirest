from rest_framework.routers import DefaultRouter
from apirest.views import *

router_apirest = DefaultRouter()

# Routes
router_apirest.register(prefix='AppPermArtAditionals', basename='AppPermArtAditionals', viewset=AppPermArtAditionals)
router_apirest.register(prefix='AppPermArtAssociatedEquipments', basename='AppPermArtAssociatedEquipments', viewset=AppPermArtAssociatedEquipments)
router_apirest.register(prefix='AppPermArtControls', basename='AppPermArtControls', viewset=AppPermArtControls)
router_apirest.register(prefix='AppPermArtCrossRegisters', basename='AppPermArtCrossRegisters', viewset=AppPermArtCrossRegisters)
router_apirest.register(prefix='AppPermArtEmployees', basename='AppPermArtEmployees', viewset=AppPermArtEmployees)
router_apirest.register(prefix='AppPermArtEppRiskStep', basename='AppPermArtEppRiskStep', viewset=AppPermArtEppRiskStep)
router_apirest.register(prefix='AppPermArtHeadAdditional', basename='AppPermArtHeadAdditional', viewset=AppPermArtHeadAdditional)
router_apirest.register(prefix='AppPermArtHeadRiskRule', basename='AppPermArtHeadRiskRule', viewset=AppPermArtHeadRiskRule)
router_apirest.register(prefix='AppPermArtHeads', basename='AppPermArtHeads', viewset=AppPermArtHeads)
router_apirest.register(prefix='AppPermArtRiskRules', basename='AppPermArtRiskRules', viewset=AppPermArtRiskRules)
router_apirest.register(prefix='AppPermArtSteps', basename='AppPermArtSteps', viewset=AppPermArtSteps)
router_apirest.register(prefix='AppPermCepActivities', basename='AppPermCepActivities', viewset=AppPermCepActivities)
router_apirest.register(prefix='AppPermCepAuthorizationStaff', basename='AppPermCepAuthorizationStaff', viewset=AppPermCepAuthorizationStaff)
router_apirest.register(prefix='AppPermCepBlockEquipments', basename='AppPermCepBlockEquipments', viewset=AppPermCepBlockEquipments)
router_apirest.register(prefix='AppPermCepEnergyTypes', basename='AppPermCepEnergyTypes', viewset=AppPermCepEnergyTypes)
router_apirest.register(prefix='AppPermCepHeadDetail', basename='AppPermCepHeadDetail', viewset=AppPermCepHeadDetail)
router_apirest.register(prefix='AppPermCepHeads', basename='AppPermCepHeads', viewset=AppPermCepHeads)
router_apirest.register(prefix='AppPermCepSpecialitiesTypes', basename='AppPermCepSpecialitiesTypes', viewset=AppPermCepSpecialitiesTypes)
router_apirest.register(prefix='AppPermCepStaffs', basename='AppPermCepStaffs', viewset=AppPermCepStaffs)
router_apirest.register(prefix='AppPermEcAssesstments', basename='AppPermEcAssesstments', viewset=AppPermEcAssesstments)
router_apirest.register(prefix='AppPermEcAutorizationEmployees', basename='AppPermEcAutorizationEmployees', viewset=AppPermEcAutorizationEmployees)
router_apirest.register(prefix='AppPermEcCategories', basename='AppPermEcCategories', viewset=AppPermEcCategories)
router_apirest.register(prefix='AppPermEcGases', basename='AppPermEcGases', viewset=AppPermEcGases)
router_apirest.register(prefix='AppPermEcHeadOptions', basename='AppPermEcHeadOptions', viewset=AppPermEcHeadOptions)
router_apirest.register(prefix='AppPermEcHeads', basename='AppPermEcHeads', viewset=AppPermEcHeads)
router_apirest.register(prefix='AppPermEcOptions', basename='AppPermEcOptions', viewset=AppPermEcOptions)
router_apirest.register(prefix='AppPermEcPermissionValidate', basename='AppPermEcPermissionValidate', viewset=AppPermEcPermissionValidate)
router_apirest.register(prefix='AppPermIzaesCapacityLoading', basename='AppPermIzaesCapacityLoading', viewset=AppPermIzaesCapacityLoading)
router_apirest.register(prefix='AppPermIzaesConditionHead', basename='AppPermIzaesConditionHead', viewset=AppPermIzaesConditionHead)
router_apirest.register(prefix='AppPermIzaesConditions', basename='AppPermIzaesConditions', viewset=AppPermIzaesConditions)
router_apirest.register(prefix='AppPermIzaesFinalLoading', basename='AppPermIzaesFinalLoading', viewset=AppPermIzaesFinalLoading)
router_apirest.register(prefix='AppPermIzaesHeads', basename='AppPermIzaesHeads', viewset=AppPermIzaesHeads)
router_apirest.register(prefix='AppPermIzaesIzajeElements', basename='AppPermIzaesIzajeElements', viewset=AppPermIzaesIzajeElements)
router_apirest.register(prefix='AppPermIzaesManeuverParameter', basename='AppPermIzaesManeuverParameter', viewset=AppPermIzaesManeuverParameter)
router_apirest.register(prefix='AppPermIzaesManeuvers', basename='AppPermIzaesManeuvers', viewset=AppPermIzaesManeuvers)
router_apirest.register(prefix='AppPermIzaesWindConditions', basename='AppPermIzaesWindConditions', viewset=AppPermIzaesWindConditions)
router_apirest.register(prefix='AppPermTaAuthorizationEmployees', basename='AppPermTaAuthorizationEmployees', viewset=AppPermTaAuthorizationEmployees)
router_apirest.register(prefix='AppPermTaCategories', basename='AppPermTaCategories', viewset=AppPermTaCategories)
router_apirest.register(prefix='AppPermTaControlMeasures', basename='AppPermTaControlMeasures', viewset=AppPermTaControlMeasures)
router_apirest.register(prefix='AppPermTaHeadControlMeasure', basename='AppPermTaHeadControlMeasure', viewset=AppPermTaHeadControlMeasure)
router_apirest.register(prefix='AppPermTaHeads', basename='AppPermTaHeads', viewset=AppPermTaHeads)
router_apirest.register(prefix='AppPermTaPermissionValidates', basename='AppPermTaPermissionValidates', viewset=AppPermTaPermissionValidates)
router_apirest.register(prefix='AppPermTaRiskDangers', basename='AppPermTaRiskDangers', viewset=AppPermTaRiskDangers)
router_apirest.register(prefix='AppPermAreas', basename='AppPermAreas', viewset=AppPermAreas)
router_apirest.register(prefix='AppPermCompanies', basename='AppPermCompanies', viewset=AppPermCompanies)
router_apirest.register(prefix='AppPermEppRisks', basename='AppPermEppRisks', viewset=AppPermEppRisks)
router_apirest.register(prefix='AppPermHeadPermission', basename='AppPermHeadPermission', viewset=AppPermHeadPermission)
router_apirest.register(prefix='AppPermPermissions', basename='AppPermPermissions', viewset=AppPermPermissions)
router_apirest.register(prefix='ActionShape', basename='ActionShape', viewset=ActionShape)
router_apirest.register(prefix='Actions', basename='Actions', viewset=Actions)
router_apirest.register(prefix='Attachments', basename='Attachments', viewset=Attachments)
router_apirest.register(prefix='Backups', basename='Backups', viewset=Backups)
router_apirest.register(prefix='Capsules', basename='Capsules', viewset=Capsules)