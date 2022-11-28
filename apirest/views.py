from apirest.models import *
from apirest.serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

class ActionShape(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ActionShapeSerializer
    queryset = ActionShape.objects.all()

class Actions(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ActionsSerializer
    queryset = Actions.objects.all()

class Attachments(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AttachmentsSerializer
    queryset = Attachments.objects.all()

class Backups(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BackupsSerializer
    queryset = Backups.objects.all()
 
class Capsules(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CapsulesSerializer
    queryset = Capsules.objects.all()

class Categories(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()

class DetailsProgress(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = DetailsProgressSerializer
    queryset = DetailsProgress.objects.all()

class EquipmentTechnicalObject(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EquipmentTechnicalObjectSerializer
    queryset = EquipmentTechnicalObject.objects.all()

class EquipmentVirtualPlant(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EquipmentVirtualPlantSerializer
    queryset = EquipmentVirtualPlant.objects.all()

class Equipments(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EquipmentsSerializer
    queryset = Equipments.objects.all()

class ExamQuestion(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ExamQuestionSerializer
    queryset = ExamQuestion.objects.all()

class ExamQuestionParents(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ExamQuestionParentsSerializer
    queryset = ExamQuestionParents.objects.all()

class ExamResults(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ExamResultsSerializer
    queryset = ExamResults.objects.all()

class ExamTypes(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ExamTypesSerializer
    queryset = ExamTypes.objects.all()

class Exams(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ExamsSerializer
    queryset = Exams.objects.all()

class FailedJobs(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FailedJobsSerializer
    queryset = FailedJobs.objects.all()

class Files(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FilesSerializer
    queryset = Files.objects.all()

class Share_File(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = Share_FileSerializer
    queryset = Share_File.objects.all()

class Historicals(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = HistoricalsSerializer
    queryset = Historicals.objects.all()

class Icons(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = IconsSerializer
    queryset = Icons.objects.all()

class Images(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ImagesSerializer
    queryset = Images.objects.all()

class Interlug(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = InterlugSerializer
    queryset = Interlug.objects.all()

class Jobs(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = JobsSerializer
    queryset = Jobs.objects.all()

class Levels(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LevelsSerializer
    queryset = Levels.objects.all()

class MapShape(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MapShapeSerializer
    queryset = MapShape.objects.all()

class MapTypes(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MapTypesSerializer
    queryset = MapTypes.objects.all()

class Maps(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MapsSerializer
    queryset = Maps.objects.all()

class Migrations(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MigrationsSerializer
    queryset = Migrations.objects.all()

class Options(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OptionsSerializer
    queryset = Options.objects.all()

class PasswordResets(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PasswordResetsSerializer
    queryset = PasswordResets.objects.all()

class PermissionRole(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PermissionRoleSerializer
    queryset = PermissionRole.objects.all()

class Permissions(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PermissionsSerializer
    queryset = Permissions.objects.all()

class PlantItem(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PlantItemSerializer
    queryset = PlantItem.objects.all()

class PlantItemFile(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PlantItemFileSerializer
    queryset = PlantItemFile.objects.all()

class Procedures(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProceduresSerializer
    queryset = Procedures.objects.all()

class Progress(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProgressSerializer
    queryset = Progress.objects.all()

class QuestionLevels(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionLevelsSerializer
    queryset = QuestionLevels.objects.all()

class QuestionResults(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionResultsSerializer
    queryset = QuestionResults.objects.all()

class Questions(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionsSerializer
    queryset = Questions.objects.all()

class RoleUser(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = RoleUserSerializer
    queryset = RoleUser.objects.all()

class Roles(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = RolesSerializer
    queryset = Roles.objects.all()

class ScoreDetails(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ScoreDetailsSerializer
    queryset = ScoreDetails.objects.all()

class Scores(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ScoresSerializer
    queryset = Scores.objects.all()

class Sessions(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SessionsSerializer
    queryset = Sessions.objects.all()

class Shapes(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ShapesSerializer
    queryset = Shapes.objects.all()

class TechnicalObjectFile(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TechnicalObjectFileSerializer
    queryset = TechnicalObjectFile.objects.all()

class TechnicalObjects(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TechnicalObjectsSerializer
    queryset = TechnicalObjects.objects.all()

class Troubleshooting(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TroubleshootingSerializer
    queryset = Troubleshooting.objects.all()

class Users(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UsersSerializer
    queryset = Users.objects.all()

class Versions(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = VersionsSerializer
    queryset = Versions.objects.all()

class VirtualPlants(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = VirtualPlantsSerializer
    queryset = VirtualPlants.objects.all()

class WebsocketsStatisticsEntries(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WebsocketsStatisticsEntriesSerializer
    queryset = WebsocketsStatisticsEntries.objects.all()