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

class Categories(ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()

class DetailsProgress(ModelViewSet):
    serializer_class = DetailsProgressSerializer
    queryset = DetailsProgress.objects.all()

class EquipmentTechnicalObject(ModelViewSet):
    serializer_class = EquipmentTechnicalObjectSerializer
    queryset = EquipmentTechnicalObject.objects.all()

class EquipmentVirtualPlant(ModelViewSet):
    serializer_class = EquipmentVirtualPlantSerializer
    queryset = EquipmentVirtualPlant.objects.all()

class Equipments(ModelViewSet):
    serializer_class = EquipmentsSerializer
    queryset = Equipments.objects.all()

class ExamQuestion(ModelViewSet):
    serializer_class = ExamQuestionSerializer
    queryset = ExamQuestion.objects.all()

class ExamQuestionParents(ModelViewSet):
    serializer_class = ExamQuestionParentsSerializer
    queryset = ExamQuestionParents.objects.all()

class ExamResults(ModelViewSet):
    serializer_class = ExamResultsSerializer
    queryset = ExamResults.objects.all()

class ExamTypes(ModelViewSet):
    serializer_class = ExamTypesSerializer
    queryset = ExamTypes.objects.all()

class Exams(ModelViewSet):
    serializer_class = ExamsSerializer
    queryset = Exams.objects.all()

class FailedJobs(ModelViewSet):
    serializer_class = FailedJobsSerializer
    queryset = FailedJobs.objects.all()

class Files(ModelViewSet):
    serializer_class = FilesSerializer
    queryset = Files.objects.all()

class Historicals(ModelViewSet):
    serializer_class = HistoricalsSerializer
    queryset = Historicals.objects.all()

class Icons(ModelViewSet):
    serializer_class = IconsSerializer
    queryset = Icons.objects.all()

class Images(ModelViewSet):
    serializer_class = ImagesSerializer
    queryset = Images.objects.all()

class Interlug(ModelViewSet):
    serializer_class = InterlugSerializer
    queryset = Interlug.objects.all()

class Jobs(ModelViewSet):
    serializer_class = JobsSerializer
    queryset = Jobs.objects.all()

class Levels(ModelViewSet):
    serializer_class = LevelsSerializer
    queryset = Levels.objects.all()

class MapShape(ModelViewSet):
    serializer_class = MapShapeSerializer
    queryset = MapShape.objects.all()

class MapTypes(ModelViewSet):
    serializer_class = MapTypesSerializer
    queryset = MapTypes.objects.all()

class Maps(ModelViewSet):
    serializer_class = MapsSerializer
    queryset = Maps.objects.all()

class Migrations(ModelViewSet):
    serializer_class = MigrationsSerializer
    queryset = Migrations.objects.all()

class Options(ModelViewSet):
    serializer_class = OptionsSerializer
    queryset = Options.objects.all()

class PasswordResets(ModelViewSet):
    serializer_class = PasswordResetsSerializer
    queryset = PasswordResets.objects.all()

class PermissionRole(ModelViewSet):
    serializer_class = PermissionRoleSerializer
    queryset = PermissionRole.objects.all()

class Permissions(ModelViewSet):
    serializer_class = PermissionsSerializer
    queryset = Permissions.objects.all()

class PlantItem(ModelViewSet):
    serializer_class = PlantItemSerializer
    queryset = PlantItem.objects.all()

class PlantItemFile(ModelViewSet):
    serializer_class = PlantItemFileSerializer
    queryset = PlantItemFile.objects.all()

class Procedures(ModelViewSet):
    serializer_class = ProceduresSerializer
    queryset = Procedures.objects.all()

class Progress(ModelViewSet):
    serializer_class = ProgressSerializer
    queryset = Progress.objects.all()

class QuestionLevels(ModelViewSet):
    serializer_class = QuestionLevelsSerializer
    queryset = QuestionLevels.objects.all()

class QuestionResults(ModelViewSet):
    serializer_class = QuestionResultsSerializer
    queryset = QuestionResults.objects.all()

class Questions(ModelViewSet):
    serializer_class = QuestionsSerializer
    queryset = Questions.objects.all()

class RoleUser(ModelViewSet):
    serializer_class = RoleUserSerializer
    queryset = RoleUser.objects.all()

class Roles(ModelViewSet):
    serializer_class = RolesSerializer
    queryset = Roles.objects.all()

class ScoreDetails(ModelViewSet):
    serializer_class = ScoreDetailsSerializer
    queryset = ScoreDetails.objects.all()

class Scores(ModelViewSet):
    serializer_class = ScoresSerializer
    queryset = Scores.objects.all()

class Sessions(ModelViewSet):
    serializer_class = SessionsSerializer
    queryset = Sessions.objects.all()

class Shapes(ModelViewSet):
    serializer_class = ShapesSerializer
    queryset = Shapes.objects.all()

class TechnicalObjectFile(ModelViewSet):
    serializer_class = TechnicalObjectFileSerializer
    queryset = TechnicalObjectFile.objects.all()

class TechnicalObjects(ModelViewSet):
    serializer_class = TechnicalObjectsSerializer
    queryset = TechnicalObjects.objects.all()

class Troubleshooting(ModelViewSet):
    serializer_class = TroubleshootingSerializer
    queryset = Troubleshooting.objects.all()

class Users(ModelViewSet):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()

class Versions(ModelViewSet):
    serializer_class = VersionsSerializer
    queryset = Versions.objects.all()

class VirtualPlants(ModelViewSet):
    serializer_class = VirtualPlantsSerializer
    queryset = VirtualPlants.objects.all()

class WebsocketsStatisticsEntries(ModelViewSet):
    serializer_class = WebsocketsStatisticsEntriesSerializer
    queryset = WebsocketsStatisticsEntries.objects.all()