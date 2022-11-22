from apirest.models import *
from apirest.serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

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