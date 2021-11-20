from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import NewsDetailSerializer
from .serializers import NewsCreateSerializer
from .models import News, Category


# для новостей достаточно ВСЕХ КЛАССОВ "из коробки" (батарейки в комплекте)


# тут под капотом post-запрос и в 2 строки создаем новость, КРУТО!
class NewsCreateView(generics.CreateAPIView):
    serializer_class = NewsCreateSerializer


# тут под капотом get-запрос
class NewsListView(generics.ListAPIView):
    serializer_class = NewsDetailSerializer
    queryset = News.objects.filter(is_published=True)


# в новостях не нужен дополнительный функционал, поэтому можем ограничиться этим
# буквально в 3 (!!!) строки кода получаем и удаление, и просмотр, и редактирование
# я просто в шоке!
class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsDetailSerializer
    queryset = News.objects.filter(is_published=True)


class NewsDetailByCategoryView(APIView):
    def get(self, request, pk):
        required_category = get_object_or_404(Category, pk=pk)
        news_by_category = News.objects.filter(is_published=True, category=required_category.pk)
        serializer = NewsDetailSerializer(news_by_category, many=True)
        return Response(serializer.data)
