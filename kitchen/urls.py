"""
URL configuration for Restaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from kitchen.views import (index,
                           DishTypeListView,
                           DishListView,
                           DishDetailView,
                           DishTypeCreateView,
                           DishTypeUpdateView,
                           DishTypeDeleteView,
                           DishCreateView,
                           DishUpdateView,
                           DishDeleteView,
                           CookListView,
                           CookCreateView,
                           CookUpdateView,
                           CookDetailView)


urlpatterns = [
    path("", index, name="index"),
    path("dish-type/create", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish-type/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-type/<int:pk>/update", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish-type/<int:pk>/delete", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish/create", DishCreateView.as_view(), name="dish-create"),
    path("dish/<int:pk>/update", DishUpdateView.as_view(), name="dish-update"),
    path("dish/<int:pk>/delete", DishDeleteView.as_view(), name="dish-delete"),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("cook/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/update", CookUpdateView.as_view(), name="cook-update"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
]


app_name = "kitchen"
