from django.urls import path
from .views import HeroStatsAPIView

from .views import (
    CategoryListAPIView,
    CategoryCreateAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
    ProductCreateAPIView,
    ProductUpdateAPIView,
    ProductDeleteAPIView,
    InquiryCreateAPIView,
    InquiryListAPIView,
    TestimonialListAPIView,
)

urlpatterns = [
    # Categories
    path("categories/", CategoryListAPIView.as_view(), name="category-list"),
    path("categories/create/", CategoryCreateAPIView.as_view(), name="category-create"),

    # Products
    path("products/", ProductListAPIView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailAPIView.as_view(), name="product-detail"),
    path("products/create/", ProductCreateAPIView.as_view(), name="product-create"),
    path("products/<int:pk>/update/", ProductUpdateAPIView.as_view(), name="product-update"),
    path("products/<int:pk>/delete/", ProductDeleteAPIView.as_view(), name="product-delete"),
    path("hero-stats/", HeroStatsAPIView.as_view()),


    # Inquiries
    path("inquiries/create/", InquiryCreateAPIView.as_view(), name="inquiry-create"),
    path("inquiries/", InquiryListAPIView.as_view(), name="inquiry-list"),


    path("testimonials/", TestimonialListAPIView.as_view()),

]
