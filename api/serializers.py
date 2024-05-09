from rest_framework import serializers
from users.models import Users, Products, City, Country, Address, Delivery, ProductTypes, Comments, Categories, PaymentTypes, PaymentStatuses, Payments, Testimonials


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('name', 'description',)


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name', )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'email', 'username', 'phone_number',)


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ('first_name', 'last_name', 'email', 'car_type', 'address', )


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name', )


class ProductTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTypes
        fields = ('name', 'price', 'description', 'rating', 'country_of_origin', )


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('name', 'description',)


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('comment', )


class PaymentTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTypes
        fields = ('name', )


class PaymentStatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentStatuses
        fields = ('name', )


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('name', )


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ("amount", 'payment_type', 'payment_status', 'product_type', )


class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = ('content', 'client_name', )