from django.shortcuts import render

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
