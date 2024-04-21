from django.urls import path
from .views import (LandingPageView, UserLoginView, UserRegisterView, ProductListView, ContactListView, UserLogOutView,
                    CartListView, CheckoutListView,TestimonialView, NotFound, ShopDetailView)


urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path("auth/login/", UserLoginView.as_view(), name="login"),
    path("auth/register/", UserRegisterView.as_view(), name="register"),
    path("products/", ProductListView.as_view(), name="products"),
    path("products/detail/<int:id>/", ShopDetailView.as_view(), name="product-detail"),
    path("contacts/", ContactListView.as_view(), name="contact"),
    path("logout/", UserLogOutView.as_view(), name="logout"),
    path("cart/", CartListView.as_view(), name="cart"),
    path("checkout/", CheckoutListView.as_view(), name="checkout"),
    path("test/", TestimonialView.as_view(), name="testimonial"),
    path("notfound/", NotFound.as_view(), name="notfound"),

]