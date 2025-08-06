from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView

from kitchen.models import Dish, Cook, DishType


def index(request):
    number_dishes = Dish.objects.count()
    number_cooks = Cook.objects.count()
    number_type_dishes = DishType.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "number_dishes": number_dishes,
        "number_cooks": number_cooks,
        "number_type_dishes": number_type_dishes,
        "num_visits": num_visits
    }
    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 5


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 5


class DishDetailView(generic.DetailView):
    model = Dish
