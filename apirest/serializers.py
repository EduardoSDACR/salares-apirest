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

class AppPermArtControlsSerializer(ModelSerializer):
    class Meta:
        model=AppPermArtControls
        fields='__all__'

class AppPermArtCrossRegistersSerializer(ModelSerializer):
    class Meta:
        model=AppPermArtCrossRegisters
        fields='__all__'

class AppPermArtEmployeesSerializer(ModelSerializer):
    class Meta:
        model=AppPermArtEmployees
        fields='__all__'

class AppPermArtEppRiskStepSerializer(ModelSerializer):
    class Meta:
        model=AppPermArtEppRiskStep
        fields='__all__'

class AppPermArtHeadAdditionalSerializer(ModelSerializer):
    class Meta:
        model=AppPermArtHeadAdditional
        fields='__all__'
        
class AppPermArtHeadRiskRuleSerializer(ModelSerializer):
    class Meta:
        model=AppPermArtHeadRiskRule
        fields='__all__'
        
class AppPermArtHeadsSerializer(ModelSerializer):
    class Meta:
        model=AppPermArtHeads
        fields='__all__'
        
class AppPermArtRiskRulesSerializer(ModelSerializer):
    class Meta:
        model=AppPermArtRiskRules
        fields='__all__'
        
class AppPermArtStepsSerializer(ModelSerializer):
    class Meta:
        model=AppPermArtSteps
        fields='__all__'
        
class AppPermCepActivitiesSerializer(ModelSerializer):
    class Meta:
        model=AppPermCepActivities
        fields='__all__'
        
class AppPermCepAuthorizationStaffSerializer(ModelSerializer):
    class Meta:
        model=AppPermCepAuthorizationStaff
        fields='__all__'
        
class AppPermCepBlockEquipmentsSerializer(ModelSerializer):
    class Meta:
        model=AppPermCepBlockEquipments
        fields='__all__'
        
class AppPermCepEnergyTypesSerializer(ModelSerializer):
    class Meta:
        model=AppPermCepEnergyTypes
        fields='__all__'
        
class AppPermCepHeadDetailSerializer(ModelSerializer):
    class Meta:
        model=AppPermCepHeadDetail
        fields='__all__'

class AppPermCepHeadsSerializer(ModelSerializer):
    class Meta:
        model=AppPermCepHeads
        fields='__all__'
        
class AppPermCepSpecialitiesTypesSerializer(ModelSerializer):
    class Meta:
        model=AppPermCepSpecialitiesTypes
        fields='__all__'
        
class AppPermCepStaffsSerializer(ModelSerializer):
    class Meta:
        model=AppPermCepStaffs
        fields='__all__'
        
class AppPermEcAssesstmentsSerializer(ModelSerializer):
    class Meta:
        model=AppPermEcAssesstments
        fields='__all__'
        
class AppPermEcAutorizationEmployeesSerializer(ModelSerializer):
    class Meta:
        model=AppPermEcAutorizationEmployees
        fields='__all__'
        
class AppPermEcCategoriesSerializer(ModelSerializer):
    class Meta:
        model=AppPermEcCategories
        fields='__all__'
        
class AppPermEcGasesSerializer(ModelSerializer):
    class Meta:
        model=AppPermEcGases
        fields='__all__'
        
class AppPermEcHeadOptionsSerializer(ModelSerializer):
    class Meta:
        model=AppPermEcHeadOptions
        fields='__all__'
        
class AppPermEcHeadsSerializer(ModelSerializer):
    class Meta:
        model=AppPermEcHeads
        fields='__all__'
        
class AppPermEcOptionsSerializer(ModelSerializer):
    class Meta:
        model=AppPermEcOptions
        fields='__all__'
        
class AppPermEcPermissionValidateSerializer(ModelSerializer):
    class Meta:
        model=AppPermEcPermissionValidate
        fields='__all__'
        
class AppPermIzaesCapacityLoadingSerializer(ModelSerializer):
    class Meta:
        model=AppPermIzaesCapacityLoading
        fields='__all__'
        
class AppPermIzaesConditionHeadSerializer(ModelSerializer):
    class Meta:
        model=AppPermIzaesConditionHead
        fields='__all__'
        
class AppPermIzaesConditionsSerializer(ModelSerializer):
    class Meta:
        model=AppPermIzaesConditions
        fields='__all__'
        
class AppPermIzaesFinalLoadingSerializer(ModelSerializer):
    class Meta:
        model=AppPermIzaesFinalLoading
        fields='__all__'
        
class AppPermIzaesHeadsSerializer(ModelSerializer):
    class Meta:
        model=AppPermIzaesHeads
        fields='__all__'
        
class AppPermIzaesIzajeElementsSerializer(ModelSerializer):
    class Meta:
        model=AppPermIzaesIzajeElements
        fields='__all__'
        
class AppPermIzaesManeuverParameterSerializer(ModelSerializer):
    class Meta:
        model=AppPermIzaesManeuverParameter
        fields='__all__'
        
class AppPermIzaesManeuversSerializer(ModelSerializer):
    class Meta:
        model=AppPermIzaesManeuvers
        fields='__all__'
        
class AppPermIzaesWindConditionsSerializer(ModelSerializer):
    class Meta:
        model=AppPermIzaesWindConditions
        fields='__all__'
        
class AppPermTaAuthorizationEmployeesSerializer(ModelSerializer):
    class Meta:
        model=AppPermTaAuthorizationEmployees
        fields='__all__'
        
class AppPermTaCategoriesSerializer(ModelSerializer):
    class Meta:
        model=AppPermTaCategories
        fields='__all__'
        
class AppPermTaControlMeasuresSerializer(ModelSerializer):
    class Meta:
        model=AppPermTaControlMeasures
        fields='__all__'
        
class AppPermTaHeadControlMeasureSerializer(ModelSerializer):
    class Meta:
        model=AppPermTaHeadControlMeasure
        fields='__all__'
        
class AppPermTaHeadsSerializer(ModelSerializer):
    class Meta:
        model=AppPermTaHeads
        fields='__all__'
        
class AppPermTaPermissionValidatesSerializer(ModelSerializer):
    class Meta:
        model=AppPermTaPermissionValidates
        fields='__all__'
        
class AppPermTaRiskDangersSerializer(ModelSerializer):
    class Meta:
        model=AppPermTaRiskDangers
        fields='__all__'
        
class AppPermAreasSerializer(ModelSerializer):
    class Meta:
        model=AppPermAreas
        fields='__all__'
        
class AppPermCompaniesSerializer(ModelSerializer):
    class Meta:
        model=AppPermCompanies
        fields='__all__'
        
class AppPermEppRisksSerializer(ModelSerializer):
    class Meta:
        model=AppPermEppRisks
        fields='__all__'

class AppPermHeadPermissionSerializer(ModelSerializer):
    class Meta:
        model=AppPermHeadPermission
        fields='__all__'
        
class AppPermPermissionsSerializer(ModelSerializer):
    class Meta:
        model=AppPermPermissions
        fields='__all__'
        
class ActionShapeSerializer(ModelSerializer):
    class Meta:
        model=ActionShape
        fields='__all__'
        
class ActionsSerializer(ModelSerializer):
    class Meta:
        model=Actions
        fields='__all__'
        
class AttachmentsSerializer(ModelSerializer):
    class Meta:
        model=Attachments
        fields='__all__'
        
class BackupsSerializer(ModelSerializer):
    class Meta:
        model=Backups
        fields='__all__'
        
class CapsulesSerializer(ModelSerializer):
    class Meta:
        model=Capsules
        fields='__all__'