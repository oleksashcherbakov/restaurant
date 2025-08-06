from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView

from kitchen.models import Dish, Cook, DishType


def index(request):
    number_dishes = Dish.objects.count()
    number_cooks = Cook.objects.count()
    number_type_dishes = DishType.objects.count()

    context = {
        "number_dishes": number_dishes,
        "number_cooks": number_cooks,
        "number_type_dishes": number_type_dishes,
    }
    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"


class DishListView(generic.ListView):
    model = Dish
