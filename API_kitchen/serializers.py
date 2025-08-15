from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

from kitchen.models import DishType, Dish, Cook


class DishTypePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 500


class DishTypeSerializer(serializers.ModelSerializer):
    pagination_class = DishTypePagination

    class Meta:
        model = DishType
        fields = ("id", "name", )


class DishTypeSerializerWithoutId(serializers.ModelSerializer):

    class Meta:
        model = DishType
        fields = ("name", )


class DishSerializer(serializers.ModelSerializer):
    dish_type = DishTypeSerializer()

    class Meta:
        model = Dish
        fields = ("id", "name", "description", "price", "is_expensive", "dish_type", "cooks", )

    def create(self, validated_data):
        dish_type_data = validated_data.pop("dish_type")
        cooks_data = validated_data.pop("cooks", [])

        dish_type_instance = DishType.objects.create(**dish_type_data)
        dish = Dish.objects.create(dish_type=dish_type_instance, **validated_data)
        dish.cooks.set(cooks_data)

        return dish


class CookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cook
        fields = ("id", "username", "email", "is_staff", "years_of_experience", )
        read_only_fields = ("is_staff", )


    def validate(self, attrs):
        if attrs["years_of_experience"] > 70:
            raise serializers.ValidationError("You can't cook more than 70 years of experience")


class CookSerializerForDishList(serializers.ModelSerializer):

    class Meta:
        model = Cook
        fields = ("username", "years_of_experience", )


class DishListSerializer(DishSerializer):
    cooks = CookSerializerForDishList(many=True)
    dish_type = DishTypeSerializerWithoutId()
