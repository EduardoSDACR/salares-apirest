from django.contrib import admin
from django.urls import path, include
from apirest.router import router_apirest
# Swagger imports
#from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Salares API",
      default_version='v1',
      description="Documentación de la API",
      #terms_of_service="https://www.google.com/policies/terms/",
      #contact=openapi.Contact(email="eduardo_sdacr@hotmail.com"),
      #license=openapi.License(name="BSD License"),
   ),
   public=True,
   #permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_apirest.urls)),
    path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
