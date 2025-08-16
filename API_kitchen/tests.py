import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Restaurant.settings")
django.setup()


from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from API_kitchen.serializers import DishTypeSerializer
from kitchen.models import Cook, Dish, DishType


def sample_dish_type():
    return DishType.objects.create(name="test_dish_type")


def sample_cook():
    return Cook.objects.create(
        username="test_cook", password="<PASSWORD>", years_of_experience=10
    )


def sample_dish():
    return Dish.objects.create(
        name="test_dish",
        description="test_description",
        price=100,
        dish_type=sample_dish_type(),
        cook=sample_cook(),
    )


class DishTypeApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username="test_admin",
            email="test_email@gmail.com",
            password="test_password",
            years_of_experience=10,
        )
        self.client.force_authenticate(self.user)

    def test_dish_type_list(self):
        DishType.objects.all().delete()
        sample_dish_type()

        res = self.client.get(reverse("API_kitchen:dishtypes-list"))
        dishes_type = DishType.objects.all()
        serializer = DishTypeSerializer(dishes_type, many=True)

        self.assertEqual(res.data["results"], serializer.data)
