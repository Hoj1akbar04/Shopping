from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import (Users, Country, Products, City, Address, Delivery, ProductTypes, Comments, Categories,
                          PaymentTypes, PaymentStatuses, Payments, Testimonials)
from api.serializers import (CountrySerializer, ProductSerializer, UserSerializer, AddressSerializer, DeliverySerializer,
                             CategoriesSerializer, CommentsSerializer, PaymentTypesSerializer, CitySerializer,
                             PaymentsSerializer, ProductTypesSerializer, CommentsSerializer, CategoriesSerializer, TestimonialsSerializer, PaymentStatusesSerializer)
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination


class CountryAPIViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )


class ProductAPIViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )


class UserAPIViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    pagination_class = LimitOffsetPagination
    search_fields = ('first_name', 'last_name', 'email', )


class CityAPIViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )


class AddressAPIViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )


class DeliveryAPIViewSet(ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name', 'email', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )


class ProductTypesAPIViewSet(ModelViewSet):
    queryset = ProductTypes.objects.all()
    serializer_class = ProductTypesSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )


class CategoriesAPIViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )


class CommentsAPIViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('comment', 'comment__users__first_name', 'comment__users__last_name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )


class PaymentTypesAPIViewSet(ModelViewSet):
    queryset = PaymentTypes.objects.all()
    serializer_class = PaymentTypesSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )


class PaymentStatusesAPIViewSet(ModelViewSet):
    queryset = PaymentStatuses.objects.all()
    serializer_class = PaymentStatusesSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )


class PaymentsAPIViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('payments__users__first_name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )


class TestimonialsAPIViewSet(ModelViewSet):
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('client_name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )

