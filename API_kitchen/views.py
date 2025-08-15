from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from rest_framework import viewsets

from API_kitchen.serializers import (
    DishTypeSerializer,
    DishSerializer,
    CookSerializer,
    DishListSerializer,
)
from kitchen.models import DishType, Dish, Cook


@extend_schema(
    description="""
    Welcome to the DishType kingdom! 🏰
    This view manages all the glorious categories of our culinary creations. Think of it
    as the 'Library of Edible Genres.' You can list all the genres or filter them
    by name, because even food has an identity crisis.
    """,
    parameters=[
        OpenApiParameter(
            name="name",
            location=OpenApiParameter.QUERY,
            description="""
            The name(s) of the dish types you're looking for.
            Because even a 'Spaghetti' needs to know it's a pasta.
            """,
            type={"type": "array", "items": {"type": "string"}},
            examples=[
                OpenApiExample(
                    "Find a specific dish type",
                    summary="Example: 'Pizza'",
                    description="Returns all dishes of type 'Pizza'.",
                    value=["Pizza"],
                ),
                OpenApiExample(
                    "Find multiple types",
                    summary="Example: 'Pasta' and 'Soup'",
                    description="Returns dishes that are either Pasta or Soup.",
                    value=["Pasta", "Soup"],
                ),
            ],
        ),
    ],
    summary="The official taxonomy of deliciousness.",
)
class DishTypeViewSet(viewsets.ModelViewSet):
    queryset = DishType.objects.all()
    serializer_class = DishTypeSerializer

    def get_queryset(self):
        queryset = DishType.objects.all()
        names = self.request.query_params.getlist("name")

        if names:
            queryset = queryset.filter(name__in=names)

        return queryset.distinct()


@extend_schema(
    parameters=[
        OpenApiParameter(
            name='price',
            description='Filter dishes by price. Returns all dishes cheaper than the given value.',
            required=False,
            type=OpenApiTypes.NUMBER,
            location=OpenApiParameter.QUERY,
            examples=[
                OpenApiExample(
                    'Find cheap dishes',
                    summary='Example: $15.00',
                    description='Finds all dishes that are cheaper than 15.00',
                    value='15.00'
                ),
            ],
        ),
        OpenApiParameter(
            name='name',
            description='Filter by a dish name',
            required=False,
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            examples=[
                OpenApiExample(
                    'Find a specific dish',
                    summary='Example: "Pasta"',
                    description='Finds all dishes with the name "Pasta"',
                    value='Pasta'
                ),
            ],
        ),
    ],
    description="""
        This is the main API for managing our culinary masterpieces.
        You can list all dishes, get details on a specific dish, or filter them
        by various criteria to find exactly what you're looking for.
    """,
    examples=[
        OpenApiExample(
            'Dish list example',
            description='Example of a typical dish list response.',
            value=[
                {
                    "id": 1,
                    "name": "Spaghetti Bolognese",
                    "description": "Classic Italian dish with a rich tomato sauce.",
                    "price": 12.50,
                    "dish_type": "Pasta"
                },
                {
                    "id": 2,
                    "name": "Margherita Pizza",
                    "description": "A simple yet delicious pizza with fresh tomatoes and mozzarella.",
                    "price": 10.00,
                    "dish_type": "Pizza"
                }
            ],
            status_codes=["200"]
        ),
    ],
    summary="A menu for the gods.",
)
class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.select_related().prefetch_related("cooks")

    def get_queryset(self):
        queryset = self.queryset
        price = self.request.query_params.get("price")

        if price:
            queryset = self.queryset.filter(price__lt=price)
            return queryset.distinct()

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return DishListSerializer

        return DishSerializer



@extend_schema(
    description="""
    The gods of the kitchen! 🧑‍🍳
    This view manages all the magnificent beings who make our food.
    You can get to know their names, their skills, and even their years of servitude
    in the culinary arts. Filter them by experience if you want to find the true
    masters of the craft.
    """,
    parameters=[
        OpenApiParameter(
            name="years_of_experience",
            location=OpenApiParameter.QUERY,
            description="""
            Filter cooks by their experience. Only returns those who have
            survived more than a given number of years in the kitchen.
            The truly battle-hardened.
            """,
            type=OpenApiTypes.INT,
            examples=[
                OpenApiExample(
                    "Find seasoned veterans",
                    summary="Example: 5 years",
                    description="Returns all cooks with 5 or more years of experience.",
                    value=5,
                ),
            ],
        ),
    ],
    summary="The Hall of Fame for Culinary Wizards.",
)
class CookViewSet(viewsets.ModelViewSet):
    queryset = Cook.objects.all()
    serializer_class = CookSerializer

    def get_queryset(self):
        queryset = self.queryset
        years_of_experience = self.request.query_params.get("years_of_experience")

        if years_of_experience:
            return queryset.filter(years_of_experience__gte=years_of_experience)

        return queryset
