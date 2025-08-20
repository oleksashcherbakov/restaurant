from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from kitchen.models import DishType, Dish, Cook

DishType.objects.all().delete()
Cook.objects.all().delete()
Dish.objects.all().delete()

DISH_TYPE_LIST_URL = reverse("kitchen:dish-type-list")


class PublicDish(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_not_required(self):
        result = self.client.get(DISH_TYPE_LIST_URL)
        self.assertEqual(result.status_code, 200)


class PrivateDish(TestCase):
    def setUp(self):
        self.user = Client()
        self.cook_for_testing = get_user_model().objects.create(
            username="test_user", password="test_password", years_of_experience=10
        )
        self.client.force_login(self.cook_for_testing)

    def test_login_required(self):
        self.dish_type_for_testing = DishType.objects.create(name="test_dish_type_1")

        url = reverse("kitchen:dish-type-update", args=(self.dish_type_for_testing.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
