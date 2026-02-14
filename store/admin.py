from django.contrib import admin
from .models import Category, Product, Inquiry,Testimonial


# -----------------------
# Category Admin
# -----------------------
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("name",)
    ordering = ("-created_at",)


# -----------------------
# Product Admin
# -----------------------
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "material",
        "price",
        "stock",
        "is_available",
        "created_at",
    )
    list_filter = ("category", "material", "is_available")
    search_fields = ("name", "description")
    ordering = ("-created_at",)
    list_editable = ("price", "stock", "is_available")
    readonly_fields = ("created_at",)


# -----------------------
# Inquiry Admin
# -----------------------
@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = (
        "customer_name",
        "product",
        "quantity",
        "email",
        "created_at",
    )
    list_filter = ("created_at",)
    search_fields = ("customer_name", "email", "message")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "rating", "is_active")
    list_filter = ("is_active",)