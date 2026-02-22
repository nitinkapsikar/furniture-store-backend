from django.db import models

class Category(models.Model):
    class Meta:
        ordering = ["-created_at"]

    name = models.CharField(max_length=100)
    image = models.URLField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        ordering = ["-created_at"]

    MATERIAL_CHOICES = (
        ("wood", "Wood"),
        ("metal", "Metal"),
        ("plastic", "Plastic"),
        ("mixed", "Mixed"),
    )

    name = models.CharField(max_length=150)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )
    material = models.CharField(
        max_length=20,
        choices=MATERIAL_CHOICES
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Price in INR"
    )

    stock = models.PositiveIntegerField()
    description = models.TextField()
    image = models.URLField(max_length=500, blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Inquiry(models.Model):
    class Meta:
        ordering = ["-created_at"]

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="inquiries"
    )
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.product.name}"
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.PositiveIntegerField(default=5)
    image = models.URLField(max_length=1000, blank=True, null=True)   # 👈 change here
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
