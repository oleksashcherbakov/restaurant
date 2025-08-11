from django.shortcuts import render
from rest_framework import viewsets

from API_kitchen.serializers import DishTypeSerializer, DishSerializer, CookSerializer
from kitchen.models import DishType, Dish, Cook


class DishTypeViewSet(viewsets.ModelViewSet):
    queryset = DishType.objects.all()
    serializer_class = DishTypeSerializer


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class CookViewSet(viewsets.ModelViewSet):
    queryset = Cook.objects.all()
    serializer_class = CookSerializer
