from django.urls import path, include

from users.views import UserAPIViewSet
from .views import LandingPageView, SongAPIViewSet, AlbumAPIViewSet, ArtistAPIViewSet, UserAPIViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


router = DefaultRouter()
router.register("songs", viewset=SongAPIViewSet)
router.register("artists", viewset=ArtistAPIViewSet)
router.register("albums", viewset=AlbumAPIViewSet)
router.register("users", viewset=UserAPIViewSet)





urlpatterns = [
    path('', LandingPageView.as_view(), name='api-landing'),
    path("", include(router.urls)),
    path('auth/', views.obtain_auth_token),
]