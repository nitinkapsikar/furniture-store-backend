from rest_framework import serializers
from .models import Category, Product, Inquiry,Testimonial
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "image",
            "is_active",
            "created_at"
        ]

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source="category.name",
        read_only=True
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "category_name",
            "material",
            "price",
            "stock",
            "description",
            "image",
            "is_available",
            "created_at"
        ]
class InquirySerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(
        source="product.name",
        read_only=True
    )

    class Meta:
        model = Inquiry
        fields = [
            "id",
            "product",
            "product_name",
            "customer_name",
            "email",
            "message",
            "quantity",
            "created_at"
        ]

class TestimonialSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Testimonial
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None
