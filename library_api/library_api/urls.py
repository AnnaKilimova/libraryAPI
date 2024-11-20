from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken import views as drf_views

schema_view = get_schema_view(
    openapi.Info(
        title="Library API",
        default_version='v1',
        description="API for managing books in the library",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token-auth/', drf_views.obtain_auth_token, name='token-auth'),
    path('api/', include('books.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

