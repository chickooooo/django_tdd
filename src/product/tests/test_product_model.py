from django.test import TestCase
from product.models import Product, User


class TestProduct(TestCase):
    """Test Product Model"""

    def setUp(self) -> None:
        """Setup for test cases"""

        # create dummy user
        user = User.objects.create(
            username="dummy",
            email="dummy@dummy.com",
            password="dummy dummy",
        )

        # create dummy product
        Product.objects.create(
            name="Smartphone",
            price=50000.00,
            user=user,
        )

    def test_create_product(self):
        """Test product creation"""

        # get product from database
        product = Product.objects.get(name="Smartphone")

        # verify product name
        self.assertEqual(product.name, "Smartphone")
        # verify product price
        self.assertEqual(product.price, 50000.00)
        # verify user is not None
        self.assertIsNotNone(product.user)

        assert product.user

        # verify user username
        self.assertEqual(product.user.username, "dummy")
        # verify user email
        self.assertEqual(product.user.email, "dummy@dummy.com")

    def test_string_representation(self):
        """Test product string representation"""

        # get product from database
        product = Product.objects.get(name="Smartphone")

        # verify string representation
        self.assertEqual(str(product), "Smartphone")
