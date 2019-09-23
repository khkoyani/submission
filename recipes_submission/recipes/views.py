from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .serializers import UserSerializer, RecipeSerializer
from rest_framework import generics, mixins, permissions, viewsets
from .models import Recipe, Ingredient, Step
from rest_framework.response import Response
from rest_framework.decorators import action

User = get_user_model()
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
# Create your views here.

class RecipeListCreateViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def list(self, request):
        query = request.GET.get('username')
        print(query)
        if query is not None:
            queryset = Recipe.objects.filter(user__username=query)
            print(queryset)
            serializer = RecipeSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            queryset = Recipe.objects.all()
            serializer = RecipeSerializer(queryset, many=True)
            return Response(serializer.data)


    def retrieve(self, request, pk=None):
        # print(request.GET.get('name'))
        queryset = Recipe.objects.all()
        obj = queryset.filter(pk=pk).first()
        serializer = RecipeSerializer(obj)
        return Response(serializer.data)
    #
    # def update(self, request, pk, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = Recipe.objects.filter(pk=pk).first()
    #     print('instance', instance, instance.ingredient_set.id, instance.steps, instance.name)
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #
    #     print('--------------')
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)

