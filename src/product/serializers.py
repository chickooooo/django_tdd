from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Product Serializer"""

    # create user_id field
    user_id = serializers.PrimaryKeyRelatedField(source="user", read_only=True)

    class Meta:
        """Serializer Meta Data"""

        model = Product
        fields = (
            "name",
            "price",
            "user_id",
            "created_at",
            "updated_at",
        )
