from django import forms
from django.contrib.auth.forms import UserCreationForm
from kitchen.models import Cook


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + ("years_of_experience",)


class DishSearchForm(forms.Form):
    dish = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "search by dish"}),
    )
