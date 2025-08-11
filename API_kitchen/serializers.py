from rest_framework import serializers

from kitchen.models import DishType, Dish, Cook


class DishTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DishType
        fields = ("id", "name", )


class DishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dish
        fields = ("id", "name", "description", "price", "is_expensive", "dish_type", "cooks", )


class CookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cook
        fields = ("id", "username", "email", "is_staff", "years_of_experience", )
        read_only_fields = ("is_staff", )
