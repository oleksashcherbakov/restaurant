from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import Dish, DishType, Cook


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "price",
        "dish_type",
    )
    list_filter = (
        "name",
        "price",
        "dish_type",
        "cooks",
    )
    search_fields = (
        "name",
        "dish_type",
        "cooks",
    )


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )
