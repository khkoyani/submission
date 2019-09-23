from django.contrib import admin
from .models import Ingredient, Recipe, Step

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Step)
# Register your models here.
