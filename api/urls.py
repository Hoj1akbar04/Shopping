from django.urls import path, include

from api.views import (CountryAPIViewSet, ProductAPIViewSet, UserAPIViewSet, CityAPIViewSet, AddressAPIViewSet,
                       DeliveryAPIViewSet, PaymentsAPIViewSet, ProductTypesAPIViewSet, CommentsAPIViewSet, CategoriesAPIViewSet,
                       PaymentStatusesAPIViewSet, PaymentTypesAPIViewSet, TestimonialsAPIViewSet)
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


router = DefaultRouter()
router.register("country", viewset=CountryAPIViewSet)
router.register("product", viewset=ProductAPIViewSet)
router.register("users", viewset=UserAPIViewSet)
router.register("city", viewset=CityAPIViewSet)
router.register("address", viewset=AddressAPIViewSet)
router.register("delivery", viewset=DeliveryAPIViewSet)
router.register("payment", viewset=PaymentsAPIViewSet)
router.register("product-type", viewset=ProductTypesAPIViewSet)
router.register("comments", viewset=CommentsAPIViewSet)
router.register("category", viewset=CategoriesAPIViewSet)
router.register("payment-status", viewset=PaymentStatusesAPIViewSet)
router.register("payment-type", viewset=PaymentTypesAPIViewSet)
router.register("testimonial", viewset=TestimonialsAPIViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path('auth/', views.obtain_auth_token),
]