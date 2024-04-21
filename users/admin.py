from django.contrib import admin
from .models import (Comments, City, Address, Delivery, Users, ProductTypes, Country,
                     Products, Categories, PaymentTypes, Payments, PaymentStatuses, Testimonials)
from import_export.admin import ImportExportModelAdmin


@admin.register(Testimonials)
class TestimonialAdmin(ImportExportModelAdmin):
    list_display = ('id', 'content', 'image', 'client_name', 'profession', 'star_rating')
    list_display_links = ('id', 'content', 'image', 'client_name', 'profession', 'star_rating')
    ordering = ('-star_rating',)


@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'last_update')
    list_display_links = ('id', 'name', 'last_update')
    ordering = ('name',)


@admin.register(Comments)
class CommentsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'comment', 'create_date')
    list_display_links = ('id', 'comment', 'create_date')
    ordering = ('id',)
    search_fields = ('comment',)


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'last_update')
    list_display_links = ('id', 'name', 'last_update')
    ordering = ('id',)


@admin.register(ProductTypes)
class ProductTypesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'rating', 'weight', 'country_of_origin', 'price_type', 'last_update')
    list_display_links = ('id', 'name', 'price', 'description', 'rating', 'weight', 'country_of_origin', 'price_type', 'last_update')
    ordering = ('id',)


@admin.register(Address)
class AddressAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'last_update')
    list_display_links = ('id', 'name', 'last_update')
    ordering = ('id',)


@admin.register(Categories)
class CategoriesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'description', 'last_update')
    list_display_links = ('id', 'name', 'description', 'last_update')
    ordering = ('id',)


@admin.register(Delivery)
class DeliveryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'car_type', 'email', 'last_update')
    list_display_links = ('id', 'first_name', 'last_name', 'car_type', 'email', 'last_update')
    ordering = ('first_name',)


@admin.register(Users)
class UsersAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'username', 'phone_number')
    list_display_links = ('id', 'first_name', 'last_name', 'email', 'username', 'phone_number')
    ordering = ('first_name',)


@admin.register(Products)
class ProductsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'description', 'last_update')
    list_display_links = ('id', 'name', 'description', 'last_update')
    ordering = ('id',)


@admin.register(PaymentTypes)
class PaymentTypesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'last_update')
    list_display_links = ('id', 'name', 'last_update')
    ordering = ('name',)


@admin.register(Payments)
class PaymentsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'amount')
    list_display_links = ('id', 'amount')
    ordering = ('id',)


@admin.register(PaymentStatuses)
class PaymentStatusAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'last_update')
    list_display_links = ('id', 'name', 'last_update')
    ordering = ('name',)