from django.urls import path, include
from .views import LandingPageView, SongAPIViewSet, AlbumAPIViewSet, ArtistAPIViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


router = DefaultRouter()
router.register("songs", viewset=SongAPIViewSet)
router.register("artists", viewset=ArtistAPIViewSet)
router.register("albums", viewset=AlbumAPIViewSet)


urlpatterns = [
    path('', LandingPageView.as_view(), name='api-landing'),
    path("", include(router.urls)),
    path('auth/', views.obtain_auth_token),
]