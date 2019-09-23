from django.contrib.auth.models import User
from .models import Ingredient, Recipe, Step
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'id']

class IngredientsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=False)
    class Meta:
        model = Ingredient
        fields = ['id', 'ingredient']

class StepSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=False)
    class Meta:
        model = Step
        fields = ['id', 'step_text']

class RecipeSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True)
    ingredients = IngredientsSerializer(many=True)
    # steps = serializers.StringRelatedField(many=True)
    # ingredients = serializers.StringRelatedField(many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Recipe
        fields = ['pk', 'name', 'user', 'steps', 'ingredients']

    def create(self, validated_data):
        # super(RecipeSerializer, self).create(self)
        ing_data = validated_data.pop('ingredients')
        steps_data = validated_data.pop('steps')
        recipe = Recipe.objects.create(**validated_data)
        for ing in ing_data:
            Ingredient.objects.create(recipe=recipe, **ing)
        for steps in steps_data:
            Step.objects.create(recipe=recipe, **steps)
        return recipe

    def get_foreign_field_data(self, validated_data, field_name):
        try:
            return validated_data.pop(field_name)
        except KeyError:
            return None

    def update_steps(self, steps_data, instance):
        if steps_data is not None:
            for i, steps in enumerate(steps_data):
                print(steps)
                if steps.get('id', None) is not None:
                    step = Step.objects.get(id=steps['id'])
                    step.step_text = steps.get('step_text', step.step_text)
                    step.recipe = instance
                    step.save()
                elif steps.get('step_text', None) is not None:
                    Step.objects.create(recipe=instance, **steps)

    def update_ingredints(self, ingredient_data, instance):
        if ingredient_data is not None:
            for i, _ing in enumerate(ingredient_data):
                if _ing['id']:
                    ingred = Ingredient.objects.get(id=_ing['id'])
                    ingred.ingredient = _ing.get('ingredient', ingred.ingredient)
                    ingred.recipe = instance
                    ingred.save()
                elif _ing.get('ingredient', None) is not None:
                    Ingredient.objects.create(recipe=instance, **_ing)


    def update(self, instance, validated_data, **kwargs):
        print('valid data', validated_data)
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        # updates foreign keys if id is provided else creates a new field
        steps_data = self.get_foreign_field_data(validated_data, 'steps')
        self.update_steps(steps_data, instance)
        ingredients_data = self.get_foreign_field_data(validated_data, 'ingredients')
        self.update_ingredints(ingredients_data, instance)

        return instance
