from django.db.models import Count
from django.db.models.functions.text import Length
from django.shortcuts import render
from rest_framework.decorators import action
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

    @action(detail=False, methods=['get'])
    def recently_updated_countries(self, request, *args, **kwargs):
        recently_updated_countries = Country.objects.order_by('-last_update')[:3]
        serialized_data = self.get_serializer(recently_updated_countries, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def countries_with_long_names(self, request):
        countries_with_long_names = Country.objects.annotate(name_length=Length('name')).filter(name_length__gt=4)[:3]
        serialized_data = self.get_serializer(countries_with_long_names, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def countries_starting_with_a(self, request, *args, **kwargs):
        countries_starting_with_a = Country.objects.filter(name__istartswith='U')[:3]
        serialized_data = self.get_serializer(countries_starting_with_a, many=True).data
        return Response(serialized_data)


class ProductAPIViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['get'])
    def products_with_description(self, request):
        products_with_description = Products.objects.exclude(description__isnull=True)[:4]
        serialized_data = self.get_serializer(products_with_description, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['get'])
    def products_starting_with_letter(self, request):
        #  "A" harfiga boshlangan mahsulotlar
        letter = "A"
        products_starting_with_letter = Products.objects.filter(name__istartswith=letter)[:4]
        serialized_data = self.get_serializer(products_starting_with_letter, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def products_without_description(self, request):
        products_without_description = Products.objects.filter(description__isnull=True)[:4]
        serialized_data = self.get_serializer(products_without_description, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)


class UserAPIViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    pagination_class = LimitOffsetPagination
    search_fields = ('first_name', 'last_name', 'email', )

    @action(detail=False, methods=['get'])
    def users_with_image(self, request):
        # Rasmga ega foydalanuvchilarni qaytaradi.
        users_with_image = Users.objects.exclude(image__isnull=True)[:3]
        serialized_data = self.get_serializer(users_with_image, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def users_with_phone_number(self, request):
        # Telefon raqami mavjud foydalanuvchilarni qaytaradi.
        users_with_phone_number = Users.objects.exclude(phone_number__isnull=True)[:3]
        serialized_data = self.get_serializer(users_with_phone_number, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def users_with_address(self, request):
        # Manzili mavjud foydalanuvchilarni qaytaradi.
        users_with_address = Users.objects.exclude(address__isnull=True)[:3]
        serialized_data = self.get_serializer(users_with_address, many=True).data
        return Response(serialized_data)


class CityAPIViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['get'])
    def recently_updated_cities(self, request):
        recently_updated_cities = City.objects.order_by('-last_update')[:3]
        serialized_data = self.get_serializer(recently_updated_cities, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def cities_in_specific_country(self, request):
        country_name = "UZB"
        cities_specific_country = City.objects.filter(country__name=country_name)[:3]
        serialized_data = self.get_serializer(cities_specific_country, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def cities_starting_with_letter(self, request):
        # "T" harfiga boshlangan shaharlar
        letter = "T"
        cities_start_letter = City.objects.filter(name__istartswith=letter)[:3]
        serialized_data = self.get_serializer(cities_start_letter, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)


class AddressAPIViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['get'])
    def recently_updated_addresses(self, request):
        recently_updated_addresses = Address.objects.order_by('-last_update')[:3]
        serialized_data = self.get_serializer(recently_updated_addresses, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def addresses_in_specific_city(self, request):
        # Masalan, "Tashkent" shahridagi manzillar
        city_name = "Tashkent"
        addresses_in_specific_city = Address.objects.filter(city__name=city_name)[:3]
        serialized_data = self.get_serializer(addresses_in_specific_city, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def addresses_starting_with_letter(self, request):
        # "A" harfiga boshlangan manzillar
        letter = "A"
        addresses_starting_with_letter = Address.objects.filter(name__istartswith=letter)[:3]
        serialized_data = self.get_serializer(addresses_starting_with_letter, many=True).data
        return Response(serialized_data)


class DeliveryAPIViewSet(ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name', 'email', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['get'])
    def recent_deliveries(self, request):
        recent_deliveries = Delivery.objects.order_by('-last_update')[:3]
        serialized_data = self.get_serializer(recent_deliveries, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def deliveries_with_specific_car_type(self, request):
        car_type = "Gentra"
        deliveries_with_specific_car_type = Delivery.objects.filter(car_type=car_type)[:3]
        serialized_data = self.get_serializer(deliveries_with_specific_car_type, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def deliveries_in_specific_city(self, request):
        city_name = "Tashkent"
        deliveries_in_specific_city = Delivery.objects.filter(address__city__name=city_name)[:3]
        serialized_data = self.get_serializer(deliveries_in_specific_city, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)


class ProductTypesAPIViewSet(ModelViewSet):
    queryset = ProductTypes.objects.all()
    serializer_class = ProductTypesSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['get'])
    def recently_updated_product_types(self, request):
        recently_updated_product_types = ProductTypes.objects.order_by('-last_update')[:5]
        serialized_data = self.get_serializer(recently_updated_product_types, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def product_types_with_image(self, request):
        product_types_with_image = ProductTypes.objects.exclude(image__isnull=True)[:5]
        serialized_data = self.get_serializer(product_types_with_image, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def product_types_with_description(self, request):
        product_types_with_description = ProductTypes.objects.exclude(description__isnull=True)[:5]
        serialized_data = self.get_serializer(product_types_with_description, many=True).data
        return Response(serialized_data)


class CategoriesAPIViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['get'])
    def categories_without_products(self, request):
        categories_without_products = Categories.objects.filter(products__isnull=True)[:5]
        serialized_data = self.get_serializer(categories_without_products, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def categories_with_description(self, request):
        categories_with_description = Categories.objects.exclude(description__isnull=True)[:6]
        serialized_data = self.get_serializer(categories_with_description, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def categories_with_products(self, request):
        categories_with_products = Categories.objects.exclude(products__isnull=True)[:2]
        serialized_data = self.get_serializer(categories_with_products, many=True).data
        return Response(serialized_data)


class CommentsAPIViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('comment', 'comment__users__first_name', 'comment__users__last_name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['get'])
    def comments_by_date(self, request):
        comments_by_date = Comments.objects.order_by('-create_date')[:5]
        serialized_data = self.get_serializer(comments_by_date, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def comments_without_users(self, request):
        comments_without_users = Comments.objects.filter(users__isnull=True)[:5]
        serialized_data = self.get_serializer(comments_without_users, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def recent_comments_of_users(self, request):
        recent_comments_of_users = Comments.objects.order_by('users__last_update')[:5]
        serialized_data = self.get_serializer(recent_comments_of_users, many=True).data
        return Response(serialized_data)


class PaymentTypesAPIViewSet(ModelViewSet):
    queryset = PaymentTypes.objects.all()
    serializer_class = PaymentTypesSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['get'])
    def recent_payment_types(self, request):
        recent_payment_types = PaymentTypes.objects.order_by('-last_update')[:5]
        serialized_data = self.get_serializer(recent_payment_types, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def payment_types_starting_with_letter(self, request):
        # "A" harfiga boshlangan to'lov turlari
        letter = "A"
        payment_types_starting_with_letter = PaymentTypes.objects.filter(name__istartswith=letter)[:4]
        serialized_data = self.get_serializer(payment_types_starting_with_letter, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def payment_types_without_update(self, request):
        payment_types_without_update = PaymentTypes.objects.filter(last_update__isnull=True)[:5]
        serialized_data = self.get_serializer(payment_types_without_update, many=True).data
        return Response(serialized_data)


class PaymentStatusesAPIViewSet(ModelViewSet):
    queryset = PaymentStatuses.objects.all()
    serializer_class = PaymentStatusesSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['get'])
    def recent_payment_statuses(self, request):
        recent_payment_statuses = PaymentStatuses.objects.order_by('-last_update')[:5]
        serialized_data = self.get_serializer(recent_payment_statuses, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def payment_statuses_starting_with_letter(self, request):
         # "P" harfiga boshlangan to'lov holatlari
        letter = "P"
        payment_statuses_starting_with_letter = PaymentStatuses.objects.filter(name__istartswith=letter)[:5]
        serialized_data = self.get_serializer(payment_statuses_starting_with_letter, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def payment_statuses_without_update(self, request):
        payment_statuses_without_update = PaymentStatuses.objects.filter(last_update__isnull=True)[:5]
        serialized_data = self.get_serializer(payment_statuses_without_update, many=True).data
        return Response(serialized_data)


class PaymentsAPIViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('payments__users__first_name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['get'])
    def payments_by_product_type(self, request):
        payments_by_product_type = Payments.objects.order_by('product_type')[:5]
        serialized_data = self.get_serializer(payments_by_product_type, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def payments_by_payment_type(self, request):
        payments_by_payment_type = Payments.objects.order_by('payment_type')[:5]
        serialized_data = self.get_serializer(payments_by_payment_type, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def payments_by_payment_status(self, request):
        payments_by_payment_status = Payments.objects.order_by('payment_status')[:5]
        serialized_data = self.get_serializer(payments_by_payment_status, many=True).data
        return Response(serialized_data)


class TestimonialsAPIViewSet(ModelViewSet):
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('client_name', )
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['get'])
    def testimonials_without_image(self, request):
        testimonials_without_image = Testimonials.objects.filter(image__isnull=True)[:5]
        serialized_data = self.get_serializer(testimonials_without_image, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def recent_testimonials(self, request):
        recent_testimonials = Testimonials.objects.order_by('-id')[:5]
        serialized_data = self.get_serializer(recent_testimonials, many=True).data
        return Response(serialized_data)

    @action(detail=False, methods=['get'])
    def testimonials_with_content_length(self, request):
        testimonials_with_content_length = Testimonials.objects.annotate(content_length=Length('content')).order_by(
            '-content_length')[:5]
        serialized_data = self.get_serializer(testimonials_with_content_length, many=True).data
        return Response(serialized_data)
