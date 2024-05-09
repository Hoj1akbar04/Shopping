from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Full API",
        description="App",
        default_version="v2",
        terms_of_service='onlineshop.com',
        contact=openapi.Contact(email='hoji@gmail.com'),
        license=openapi.License(name='demo')
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ]
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("users.urls")),
    path("api/v2/", include("music.urls")),
    path("api/v1/", include("api.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('docs-swagger/', schema_view.with_ui("swagger", cache_timeout=0), name='swagger'),
    path('docs-redoc/', schema_view.with_ui("redoc", cache_timeout=0), name='redoc'),
    #path("", include("products.urls"))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)