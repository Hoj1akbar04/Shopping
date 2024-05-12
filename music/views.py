from django.db.models import Count
from django.db.transaction import atomic
from django.shortcuts import render
from rest_framework.decorators import action
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

    @action(detail=False, methods=['get'])
    def count(self, request):
        count = Artist.objects.count()
        return Response({"count": count}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def latest_artists(self, request):
        latest_artists = Artist.objects.order_by('-create_date')[:5]
        serialized_data = self.get_serializer(latest_artists, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def artist_stats(self, request):
        total_count = Artist.objects.count()
        top_names = Artist.objects.values('name').annotate(count=Count('name')).order_by('-count')[:5]
        response_data = {
            "total_count": total_count,
            "top_names": top_names
        }
        return Response(response_data)


class AlbumAPIViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'artist__name')
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['get'])
    def new_album(self, request):
        # Eng so'nggi yangi chiqqan 3 album
        new_created = Album.objects.order_by('-create_date')[:3]
        serialized_data = self.get_serializer(new_created, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def watch(self, request, *args, **kwargs):
        album = self.get_object()
        with atomic():
            album.watching += 1
            album.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def popular_albums(self, request):
        # Eng ko'p ko'rilgan 3 album
        popular_albums = Album.objects.annotate(num_tracks=Count('watching')).order_by('-watching')[:3]
        serialized_data = self.get_serializer(popular_albums, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)


class SongAPIViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    pagination_class = LimitOffsetPagination
    search_fields = ('title', 'album__title', 'album__artist__name',)
    #permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['get'])
    def listening(self, request, *args, **kwargs):
        song = self.get_object()
        with atomic():
            song.listened += 1
            song.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def tops(self, request, *args, **kwargs):
        songs = self.get_queryset()
        songs = songs.order_by('-listened')[:1]
        serializer = SongSerializer(songs, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=['post'])
    def album(self, request, *args, **kwargs):
        song = self.get_object()
        album = song.album
        serializer = AlbumSerializer(album)
        return Response(data=serializer.data)

    @action(detail=True, methods=['post'])
    def artist(self, request, *args, **kwargs):
        song = self.get_object()
        artist = song.album.artist
        serializer = ArtistSerializer(artist)
        return Response(data=serializer.data)



