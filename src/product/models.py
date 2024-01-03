from __future__ import annotations
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """Product Model"""

    # product name
    name = models.CharField(max_length=255)
    # product price
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # user who listed the product
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # datetime at which product was listed
    created_at = models.DateTimeField(default=timezone.now)
    # datetime at which product was updated
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        """String Representation"""

        # return product name
        return self.name

    @staticmethod
    def from_dict(data: dict) -> Product:
        """Create product from dictionary"""

        # verify user_id is present in data
        assert "user_id" in data, "user_id not present"
        # verify user_id is an integer
        assert type(data["user_id"]) is int, "user_id is not an integer"

        # get user with user id
        user = User.objects.get(id=data["user_id"])

        # verify user is present
        assert user is not None, f"invalid user_id: '{data['user_id']}'"

        # remove user_id from data
        del data["user_id"]

        # create and return product
        return Product(user=user, **data)
