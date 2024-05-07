from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Song, Artist, Album
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination


class LandingPageView(APIView):
    def get(self, request):
        return Response(data={'get api': 'Hello music lovers !'})

    def post(self, request):
        return Response(data={'post api': 'Hello music'})


class ArtistAPIViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )


class AlbumAPIViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'artist__name')
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )


class SongAPIViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    pagination_class = LimitOffsetPagination
    search_fields = ('title', 'album__title', 'album__artist__name',)
    #permission_classes = (IsAuthenticated,)




