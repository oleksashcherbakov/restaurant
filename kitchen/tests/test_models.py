from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import DishType, Dish, Cook

DishType.objects.all().delete()
Cook.objects.all().delete()
Dish.objects.all().delete()

dish_type_for_testing = DishType.objects.create(name="test_dish_type_1")
dish_for_testing = Dish.objects.create(
    name="test_10",
    description="test_description",
    price=50,
    dish_type=dish_type_for_testing,
)
cook_for_testing = get_user_model().objects.create(
    username="test_user", password="test_password", years_of_experience=10
)


class ModelsTests(TestCase):
    def test_dish_type_str(self):
        self.assertEqual(str(dish_type_for_testing), dish_type_for_testing.name)

    def test_dish_str(self):
        self.assertEqual(str(dish_for_testing), dish_for_testing.name)

    def test_cook_str(self):
        self.assertEqual(
            str(cook_for_testing),
            f"username: {cook_for_testing.username}, experience: {cook_for_testing.years_of_experience}",
        )

    def test_dish_property(self):
        self.assertEqual(dish_for_testing.is_expensive, False)
