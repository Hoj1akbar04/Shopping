from django.db import models
from . helpers import Choices, SaveMediaFile


class Country(models.Model):
    name = models.CharField(max_length=100)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    car_type = models.CharField(max_length=40)
    email = models.EmailField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Users(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    image = models.ImageField(upload_to=SaveMediaFile.user_image)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=10, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.username}"


class Products(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=SaveMediaFile.product_image)
    description = models.TextField()
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductTypes(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    price_type = models.CharField(max_length=8, choices=Choices.PriceType.choices, default=Choices.PriceType.s)
    image = models.ImageField(upload_to=SaveMediaFile.product_type_image)
    description = models.TextField()
    rating = models.IntegerField()
    users = models.ManyToManyField(Users)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    country_of_origin = models.CharField(max_length=50, blank=True)
    weight = models.FloatField()
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.description} {self.price} {self.country_of_origin}"


class Categories(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.description}"


class Comments(models.Model):
    comment = models.TextField()
    create_date = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(Users)

    def __str__(self):
        return f"{self.comment} {self.create_date}"


class PaymentTypes(models.Model):
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PaymentStatuses(models.Model):
    name = models.CharField(max_length=30)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Payments(models.Model):
    amount = models.FloatField()
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductTypes, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(PaymentTypes, on_delete=models.CASCADE)
    payment_status = models.ForeignKey(PaymentStatuses, on_delete=models.CASCADE)

    def __str__(self):
        return self.amount


class Testimonials(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to=SaveMediaFile.testimonial)
    client_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    star_rating = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.client_name
