from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from users.models import Products, ProductTypes, Payments, PaymentStatuses, Comments, Categories, Testimonials
from .forms import UserLoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .serializers import AddressSerializer, UserSerializer, ProductSerializer, ProductTypeSerializer, CountrySerializer, CitySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Country, City, Address, Products, ProductTypes, Users
from rest_framework import viewsets


class UserAPIViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )


class ProductTypeAPIViewSet(viewsets.ModelViewSet):
    queryset = ProductTypes.objects.all
    serializer_class = ProductTypeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )


class ProductAPIViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )


class CountryAPIViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all
    serializer_class = CountrySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )


class CityAPIViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all
    serializer_class = CitySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )


class AddressAPIViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all
    serializer_class = AddressSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )


class LandingPageView(View):
    def get(self, request):
        products = Products.objects.all()
        users = User.objects.all()
        testimonials = Testimonials.objects.all()
        context = {
            'testimonials': testimonials,
            'products': products,
            "users": users,

        }

        return render(request, 'main/index.html', context)


class UserRegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')

        if password_1 == password_2:
            user_check = User.objects.filter(username=username, password=password_1)
            if user_check:
                return render(request, "auth/register.html")
            else:
                user = User(first_name=first_name, last_name=last_name, email=email, username=username)
                user.set_password(password_1)
                user.save()
                return redirect("login")
        else:
            return render(request, "auth/register.html")


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        context = {
            "form": form
        }
        return render(request, "auth/login.html", context)

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        data = {
            "username": username,
            "password": password
        }
        login_form = AuthenticationForm(data=data)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("landing")

        else:
            form = UserLoginForm()
            context = {
                "form": form
            }
            return render(request, "auth/login.html", context)


class UserLogOutView(View):
    def get(self, request):
        logout(request)
        return redirect("landing")


class ProductListView(View):
    def get(self, request):
        search = request.GET.get("search")
        products = Products.objects.all()

        if search:
            products = products.filter(name__icontains=search)

        context = {
            "products": products,
            'search': search,
        }
        return render(request, "main/shop.html", context)

    def post(self, request):
        search = request.POST.get("search")
        products = Products.objects.all()

        if search:
            products = products.filter(name__icontains=search)

        context = {
            "products": products,
            'search': search,
        }
        return render(request, "main/shop.html", context)


class ContactListView(View):
    def get(self, request):
        return render(request, 'main/contact.html')


class CartListView(View):
    def get(self, request):
        return render(request, 'main/cart.html')


class CheckoutListView(View):
    def get(self, request):
        return render(request, 'main/chackout.html')


class TestimonialView(View):
    def get(self, request):
        testimonials = Testimonials.objects.all()
        context = {
            'testimonials': testimonials
        }
        return render(request, 'main/testimonial.html', context)


class NotFound(View):
    def get(self, request):
        return render(request, 'main/404.html')


class ShopDetailView(View):
    def get(self, request, id):
        products = Products.objects.get(id=id)
        context = {
            'product': products
        }
        return render(request, 'main/shop-detail.html', context)