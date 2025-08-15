from rest_framework import viewsets

from API_kitchen.serializers import DishTypeSerializer, DishSerializer, CookSerializer, DishListSerializer
from kitchen.models import DishType, Dish, Cook


class DishTypeViewSet(viewsets.ModelViewSet):
    queryset = DishType.objects.all()
    serializer_class = DishTypeSerializer

    def get_queryset(self):
        queryset = DishType.objects.all()
        names = self.request.query_params.getlist("name")

        if names:
            queryset = queryset.filter(name__in=names)

        return queryset.distinct()


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


class CookViewSet(viewsets.ModelViewSet):
    queryset = Cook.objects.all()
    serializer_class = CookSerializer

    def get_queryset(self):
        queryset = self.queryset
        years_of_experience = self.request.query_params.get("years_of_experience")

        if years_of_experience:
            return queryset.filter(years_of_experience__gte=years_of_experience)

        return queryset