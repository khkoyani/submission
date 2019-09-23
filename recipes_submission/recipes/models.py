from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Recipe(models.Model):
    name = models.CharField(max_length=160, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} by {self.user}'

    def __repr__(self):
        return f'<Recipe: {self.name}, {self.user}>'


class Step(models.Model):
    step_text = models.CharField(max_length=160, blank=False, null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='steps')

    def __str__(self):
        return f'{self.step_text}'

    def __repr__(self):
        return f'<Step: {self.step_text[:20]}>'

class Ingredient(models.Model):
    ingredient = models.CharField(max_length=160, blank=False, null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return f'{self.ingredient}'

    def __repr__(self):
        return f'<Step: {self.ingredient}>'
# Create your models here.
