from apirest.models import *
from apirest.serializers import *
from rest_framework.viewsets import ModelViewSet

class AppPermArtAditionals(ModelViewSet):    
    serializer_class = AppPermArtAditionalsSerializer
    queryset = AppPermArtAditionals.objects.all()

class AppPermArtAssociatedEquipments(ModelViewSet):
    serializer_class = AppPermArtAssociatedEquipmentsSerializer
    queryset = AppPermArtAssociatedEquipments.objects.all()

class AppPermArtControls(ModelViewSet):
    serializer_class = AppPermArtControlsSerializer
    queryset = AppPermArtControls.objects.all()

class AppPermArtCrossRegisters(ModelViewSet):
    serializer_class = AppPermArtCrossRegistersSerializer
    queryset = AppPermArtCrossRegisters.objects.all()

class AppPermArtEmployees(ModelViewSet):
    serializer_class = AppPermArtEmployeesSerializer
    queryset = AppPermArtEmployees.objects.all()

class AppPermArtEppRiskStep(ModelViewSet):
    serializer_class = AppPermArtEppRiskStepSerializer
    queryset = AppPermArtEppRiskStep.objects.all()

class AppPermArtHeadAdditional(ModelViewSet):
    serializer_class = AppPermArtHeadAdditionalSerializer
    queryset = AppPermArtHeadAdditional.objects.all()
    
class AppPermArtHeadRiskRule(ModelViewSet):
    serializer_class = AppPermArtHeadRiskRuleSerializer
    queryset = AppPermArtHeadRiskRule.objects.all()
    
class AppPermArtHeads(ModelViewSet):
    serializer_class = AppPermArtHeadsSerializer
    queryset = AppPermArtHeads.objects.all()
    
class AppPermArtRiskRules(ModelViewSet):
    serializer_class = AppPermArtRiskRulesSerializer
    queryset = AppPermArtRiskRules.objects.all()
    
class AppPermArtSteps(ModelViewSet):
    serializer_class = AppPermArtStepsSerializer
    queryset = AppPermArtSteps.objects.all()
    
class AppPermCepActivities(ModelViewSet):
    serializer_class = AppPermCepActivitiesSerializer
    queryset = AppPermCepActivities.objects.all()

class AppPermCepAuthorizationStaff(ModelViewSet):
    serializer_class = AppPermCepAuthorizationStaffSerializer
    queryset = AppPermCepAuthorizationStaff.objects.all()

class AppPermCepBlockEquipments(ModelViewSet):
    serializer_class = AppPermCepBlockEquipmentsSerializer
    queryset = AppPermCepBlockEquipments.objects.all()

class AppPermCepEnergyTypes(ModelViewSet):
    serializer_class = AppPermCepEnergyTypesSerializer
    queryset = AppPermCepEnergyTypes.objects.all()

class AppPermCepHeadDetail(ModelViewSet):
    serializer_class = AppPermCepHeadDetailSerializer
    queryset = AppPermCepHeadDetail.objects.all()

class AppPermCepHeads(ModelViewSet):
    serializer_class = AppPermCepHeadsSerializer
    queryset = AppPermCepHeads.objects.all()

class AppPermCepSpecialitiesTypes(ModelViewSet):
    serializer_class = AppPermCepSpecialitiesTypesSerializer
    queryset = AppPermCepSpecialitiesTypes.objects.all()

class AppPermCepStaffs(ModelViewSet):
    serializer_class = AppPermCepStaffsSerializer
    queryset = AppPermCepStaffs.objects.all()

class AppPermEcAssesstments(ModelViewSet):
    serializer_class = AppPermEcAssesstmentsSerializer
    queryset = AppPermEcAssesstments.objects.all()

class AppPermEcAutorizationEmployees(ModelViewSet):
    serializer_class = AppPermEcAutorizationEmployeesSerializer
    queryset = AppPermEcAutorizationEmployees.objects.all()

class AppPermEcCategories(ModelViewSet):
    serializer_class = AppPermEcCategoriesSerializer
    queryset = AppPermEcCategories.objects.all()

class AppPermEcGases(ModelViewSet):
    serializer_class = AppPermEcGasesSerializer
    queryset = AppPermEcGases.objects.all()

class AppPermEcHeadOptions(ModelViewSet):
    serializer_class = AppPermEcHeadOptionsSerializer
    queryset = AppPermEcHeadOptions.objects.all()

class AppPermEcHeads(ModelViewSet):
    serializer_class = AppPermEcHeadsSerializer
    queryset = AppPermEcHeads.objects.all()

class AppPermEcOptions(ModelViewSet):
    serializer_class = AppPermEcOptionsSerializer
    queryset = AppPermEcOptions.objects.all()

class AppPermEcPermissionValidate(ModelViewSet):
    serializer_class = AppPermEcPermissionValidateSerializer
    queryset = AppPermEcPermissionValidate.objects.all()

class AppPermIzaesCapacityLoading(ModelViewSet):
    serializer_class = AppPermIzaesCapacityLoadingSerializer
    queryset = AppPermIzaesCapacityLoading.objects.all()

class AppPermIzaesConditionHead(ModelViewSet):
    serializer_class = AppPermIzaesConditionHeadSerializer
    queryset = AppPermIzaesConditionHead.objects.all()

class AppPermIzaesConditions(ModelViewSet):
    serializer_class = AppPermIzaesConditionsSerializer
    queryset = AppPermIzaesConditions.objects.all()

class AppPermIzaesFinalLoading(ModelViewSet):
    serializer_class = AppPermIzaesFinalLoadingSerializer
    queryset = AppPermIzaesFinalLoading.objects.all()

class AppPermIzaesHeads(ModelViewSet):
    serializer_class = AppPermIzaesHeadsSerializer
    queryset = AppPermIzaesHeads.objects.all()

class AppPermIzaesIzajeElements(ModelViewSet):
    serializer_class = AppPermIzaesIzajeElementsSerializer
    queryset = AppPermIzaesIzajeElements.objects.all()

class AppPermIzaesManeuverParameter(ModelViewSet):
    serializer_class = AppPermIzaesManeuverParameterSerializer
    queryset = AppPermIzaesManeuverParameter.objects.all()

class AppPermIzaesManeuvers(ModelViewSet):
    serializer_class = AppPermIzaesManeuversSerializer
    queryset = AppPermIzaesManeuvers.objects.all()

class AppPermIzaesWindConditions(ModelViewSet):
    serializer_class = AppPermIzaesWindConditionsSerializer
    queryset = AppPermIzaesWindConditions.objects.all()

class AppPermTaAuthorizationEmployees(ModelViewSet):
    serializer_class = AppPermTaAuthorizationEmployeesSerializer
    queryset = AppPermTaAuthorizationEmployees.objects.all()

class AppPermTaCategories(ModelViewSet):
    serializer_class = AppPermTaCategoriesSerializer
    queryset = AppPermTaCategories.objects.all()

class AppPermTaControlMeasures(ModelViewSet):
    serializer_class = AppPermTaControlMeasuresSerializer
    queryset = AppPermTaControlMeasures.objects.all()

class AppPermTaHeadControlMeasure(ModelViewSet):
    serializer_class = AppPermTaHeadControlMeasureSerializer
    queryset = AppPermTaHeadControlMeasure.objects.all()

class AppPermTaHeads(ModelViewSet):
    serializer_class = AppPermTaHeadsSerializer
    queryset = AppPermTaHeads.objects.all()

class AppPermTaPermissionValidates(ModelViewSet):
    serializer_class = AppPermTaPermissionValidatesSerializer
    queryset = AppPermTaPermissionValidates.objects.all()

class AppPermTaRiskDangers(ModelViewSet):
    serializer_class = AppPermTaRiskDangersSerializer
    queryset = AppPermTaRiskDangers.objects.all()

class AppPermAreas(ModelViewSet):
    serializer_class = AppPermAreasSerializer
    queryset = AppPermAreas.objects.all()

class AppPermCompanies(ModelViewSet):
    serializer_class = AppPermCompaniesSerializer
    queryset = AppPermCompanies.objects.all()

class AppPermEppRisks(ModelViewSet):
    serializer_class = AppPermEppRisksSerializer
    queryset = AppPermEppRisks.objects.all()

class AppPermHeadPermission(ModelViewSet):
    serializer_class = AppPermHeadPermissionSerializer
    queryset = AppPermHeadPermission.objects.all()

class AppPermPermissions(ModelViewSet):
    serializer_class = AppPermPermissionsSerializer
    queryset = AppPermPermissions.objects.all()

class ActionShape(ModelViewSet):
    serializer_class = ActionShapeSerializer
    queryset = ActionShape.objects.all()

class Actions(ModelViewSet):
    serializer_class = ActionsSerializer
    queryset = Actions.objects.all()

class Attachments(ModelViewSet):
    serializer_class = AttachmentsSerializer
    queryset = Attachments.objects.all()

class Backups(ModelViewSet):
    serializer_class = BackupsSerializer
    queryset = Backups.objects.all()
 
class Capsules(ModelViewSet):
    serializer_class = CapsulesSerializer
    queryset = Capsules.objects.all()