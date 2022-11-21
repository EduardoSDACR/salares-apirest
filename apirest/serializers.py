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

class CategoriesSerializer(ModelSerializer):
    class Meta:
        model=Categories
        fields='__all__'

class DetailsProgressSerializer(ModelSerializer):
    class Meta:
        model=DetailsProgress
        fields='__all__'
    
class EquipmentTechnicalObjectSerializer(ModelSerializer):
    class Meta:
        model=EquipmentTechnicalObject
        fields='__all__'

class EquipmentVirtualPlantSerializer(ModelSerializer):
    class Meta:
        model=EquipmentVirtualPlant
        fields='__all__'

class EquipmentsSerializer(ModelSerializer):
    class Meta:
        model=Equipments
        fields='__all__'

class ExamQuestionSerializer(ModelSerializer):
    class Meta:
        model=ExamQuestion
        fields='__all__'

class ExamQuestionParentsSerializer(ModelSerializer):
    class Meta:
        model=ExamQuestionParents
        fields='__all__'

class ExamResultsSerializer(ModelSerializer):
    class Meta:
        model=ExamResults
        fields='__all__'

class ExamTypesSerializer(ModelSerializer):
    class Meta:
        model=ExamTypes
        fields='__all__'

class ExamsSerializer(ModelSerializer):
    class Meta:
        model=Exams
        fields='__all__'

class FailedJobsSerializer(ModelSerializer):
    class Meta:
        model=FailedJobs
        fields='__all__'

class FilesSerializer(ModelSerializer):
    class Meta:
        model=Files
        fields='__all__'

class HistoricalsSerializer(ModelSerializer):
    class Meta:
        model=Historicals
        fields='__all__'

class IconsSerializer(ModelSerializer):
    class Meta:
        model=Icons
        fields='__all__'

class ImagesSerializer(ModelSerializer):
    class Meta:
        model=Images
        fields='__all__'

class InterlugSerializer(ModelSerializer):
    class Meta:
        model=Interlug
        fields='__all__'
    
class JobsSerializer(ModelSerializer):
    class Meta:
        model=Jobs
        fields='__all__'

class LevelsSerializer(ModelSerializer):
    class Meta:
        model=Levels
        fields='__all__'

class MapShapeSerializer(ModelSerializer):
    class Meta:
        model=MapShape
        fields='__all__'

class MapTypesSerializer(ModelSerializer):
    class Meta:
        model=MapTypes
        fields='__all__'

class MapsSerializer(ModelSerializer):
    class Meta:
        model=Maps
        fields='__all__'

class MigrationsSerializer(ModelSerializer):
    class Meta:
        model=Migrations
        fields='__all__'

class OptionsSerializer(ModelSerializer):
    class Meta:
        model=Options
        fields='__all__'

class PasswordResetsSerializer(ModelSerializer):
    class Meta:
        model=PasswordResets
        fields='__all__'

class PermissionRoleSerializer(ModelSerializer):
    class Meta:
        model=PermissionRole
        fields='__all__'

class PermissionsSerializer(ModelSerializer):
    class Meta:
        model=Permissions
        fields='__all__'

class PlantItemSerializer(ModelSerializer):
    class Meta:
        model=PlantItem
        fields='__all__'

class PlantItemFileSerializer(ModelSerializer):
    class Meta:
        model=PlantItemFile
        fields='__all__'

class ProceduresSerializer(ModelSerializer):
    class Meta:
        model=Procedures
        fields='__all__'

class ProgressSerializer(ModelSerializer):
    class Meta:
        model=Progress
        fields='__all__'

class QuestionLevelsSerializer(ModelSerializer):
    class Meta:
        model=QuestionLevels
        fields='__all__'

class QuestionResultsSerializer(ModelSerializer):
    class Meta:
        model=QuestionResults
        fields='__all__'

class QuestionsSerializer(ModelSerializer):
    class Meta:
        model=Questions
        fields='__all__'

class RoleUserSerializer(ModelSerializer):
    class Meta:
        model=RoleUser
        fields='__all__'

class RolesSerializer(ModelSerializer):
    class Meta:
        model=Roles
        fields='__all__'

class ScoreDetailsSerializer(ModelSerializer):
    class Meta:
        model=ScoreDetails
        fields='__all__'

class ScoresSerializer(ModelSerializer):
    class Meta:
        model=Scores
        fields='__all__'

class SessionsSerializer(ModelSerializer):
    class Meta:
        model=Sessions
        fields='__all__'

class ShapesSerializer(ModelSerializer):
    class Meta:
        model=Shapes
        fields='__all__'

class TechnicalObjectFileSerializer(ModelSerializer):
    class Meta:
        model=TechnicalObjectFile
        fields='__all__'

class TechnicalObjectsSerializer(ModelSerializer):
    class Meta:
        model=TechnicalObjects
        fields='__all__'

class TroubleshootingSerializer(ModelSerializer):
    class Meta:
        model=Troubleshooting
        fields='__all__'

class UsersSerializer(ModelSerializer):
    class Meta:
        model=Users
        fields='__all__'

class VersionsSerializer(ModelSerializer):
    class Meta:
        model=Versions
        fields='__all__'

class VirtualPlantsSerializer(ModelSerializer):
    class Meta:
        model=VirtualPlants
        fields='__all__'

class WebsocketsStatisticsEntriesSerializer(ModelSerializer):
    class Meta:
        model=WebsocketsStatisticsEntries
        fields='__all__'

class AppPermAreasSerializer(ModelSerializer):
    class Meta:
        model=AppPermAreas
        fields='__all__'
