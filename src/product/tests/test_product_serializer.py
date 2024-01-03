from decimal import Decimal
from datetime import datetime
from django.test import TestCase
from django.utils import timezone
from product.models import Product, User
from product.serializers import ProductSerializer


class TestProductSerializer(TestCase):
    """Test Product Serializer"""

    # date format
    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f%z"

    def setUp(self) -> None:
        """Setup for test cases"""

        # create dummy user
        self.user = User.objects.create(
            username="dummy",
            email="dummy@dummy.com",
            password="dummy dummy",
        )

        # create dummy product
        self.product = Product.objects.create(
            name="Smartphone",
            price=50000.00,
            user=self.user,
        )

    def __datetime_str_to_datetime(self, datetime_str: str) -> datetime:
        """Convert datetime string to datetime object"""

        # return parsed string
        return datetime.strptime(datetime_str, self.DATE_FORMAT)

    def __datetime_to_string(self, given_datetime: datetime) -> str:
        """Convert datetime object to datetime string"""

        # return parsed datetime
        return datetime.strftime(given_datetime, self.DATE_FORMAT)

    def test_product_serialization(self):
        """Test product serialization"""

        # serialize product
        product_serialized = ProductSerializer(self.product)
        # get serialized data
        data: dict = dict(product_serialized.data)

        # verify name
        self.assertEqual(data.get("name"), self.product.name)
        # verify price
        self.assertEqual(
            Decimal(data.get("price", "")),
            self.product.price,
        )
        # verify user id
        self.assertEqual(data.get("user_id"), self.user.id)  # type: ignore
        # verify created at time
        self.assertEqual(
            self.__datetime_str_to_datetime(data.get("created_at", "")),
            self.product.created_at,
        )
        # verify updated at time
        self.assertEqual(
            self.__datetime_str_to_datetime(data.get("updated_at", "")),
            self.product.updated_at,
        )

    def test_product_deserialization(self):
        """Test product deserialization"""

        # serialized data
        data: dict = {
            "name": "Apple",
            "price": 60000.00,
            "user_id": 1,
            "created_at": self.__datetime_to_string(timezone.now()),
            "updated_at": self.__datetime_to_string(timezone.now()),
        }

        # create product object
        product = Product.from_dict(data)

        # verify type of product
        self.assertIsInstance(product, Product)
        # verify product name
        self.assertEqual(product.name, "Apple")
        # verify product price
        self.assertEqual(
            Decimal(product.price),
            60000.00,
        )

        # verify user
        assert isinstance(product.user, User)

        # verify user id
        self.assertEqual(product.user.id, 1)  # type: ignore
        # verify username
        self.assertEqual(product.user.username, "dummy")
        # verify user email
        self.assertEqual(product.user.email, "dummy@dummy.com")
