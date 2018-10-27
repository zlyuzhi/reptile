from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
import json

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from index.models import *


# Create your views here.
class BooksView(View):
    def get(self, request):
        # 查询数据
        books = BookInfo.objects.all()
        # 将图书对象转为字典（使用序列器）

        # 1 构造序列化器对象
        books_serializer = BookInfoSerializer(books, many=True)
        # 2 通过data属性可以获取序列化后的数据
        book_dict_list = books_serializer.data
        # 返回响应
        return JsonResponse(book_dict_list, safe=False)

    def post(self, request):
        # 接受
        json_byte = request.body
        json_str = json_byte.decode()
        json_dict = json.loads(json_str)
        # 验证
        book_seraliser = BookInfoSerializer(data=json_dict)
        if not book_seraliser.is_valid():
            return JsonResponse(book_seraliser.errors)
        # 保存
        book = book_seraliser.save()  # 调用了序列化器中的create

        # 响应(对象保存成字典（使用序列器）)
        book_seraliser = BookInfoSerializer(book)
        book_dict = book_seraliser.data
        return JsonResponse(book_dict, status=200)


class BookView(View):
    def put(self, request, pk):
        # 用于修改
        # 查询
        book = BookInfo.objects.get(pk=pk)

        # 接受
        json_bytes = request.body
        json_str = json_bytes.decode()
        json_dict = json.loads(json_str)

        # 验证(使用is_valid)
        book_serializer = BookInfoSerializer(book, data=json_dict)
        if not book_serializer.is_valid():
            return JsonResponse(book_serializer.errors)

        # 保存（调用序列化器中的定义的函数)
        book = book_serializer.save()  # 调用了序列化器中的create

        # 响应
        book_serializer = BookInfoSerializer(book)
        book_dict = book_serializer.data
        return JsonResponse(book_dict, status=201)


class HerosAPIView(APIView):
    def get(self, request):
        # 查询数据
        # hero=HerroInfo.objects.all()
        # 接收参数
        id = request.query_params.get('id')
        hero_list = HerroInfo.objects.filter(pk__lt=id)

        # 序列化
        hero_serializer = HeroInfoModelSerializer(hero_list, many=True)
        hero_dict_list = hero_serializer.data
        # 响应
        return Response(hero_dict_list)

    def post(self, request):
        pass
        # 接收
        hero_dict = request.data
        # 验证
        hero_serializer = HeroInfoModelSerializer(data=hero_dict)
        if not hero_serializer.is_valid():
            return Response(hero_serializer.errors)
        # 保存
        hero = hero_serializer.save()
        # 响应
        hero_serializer = HeroInfoModelSerializer(hero)
        hero_dict = hero_serializer.data
        return Response(hero_dict, status=201)


class HeroAPIView(APIView):
    # 修改
    def put(self, request, pk):
        pass
        # 根据Pk查询出要修改的对象
        try:
            hero = HerroInfo.objects.filter(pk=pk)
        except:
            return Response({'msg': '查询英雄失败'})
        # 接收 这个要修改的数据
        hero_dict = request.data  # (.data用于接收请求体中的数据)
        # 验证
        hero_serializer = HeroInfoModelSerializer(hero, data=hero_dict)
        if not hero_serializer.is_valid():
            return Response(hero_serializer.errors)
        # 保存
        hero = hero_serializer.save()
        # 响应
        hero_serializer =HeroInfoModelSerializer(hero)
        hero_dict =hero_serializer.data
        return Response(hero_dict,status=201)
    def get(self,request,pk):
        #查询数据
        try:
            hero=HerroInfo.objects.get(pk=pk)
        except:
            return Response({'msg':'查询数据失败'})
        #序列化
        hero_serializer=HeroInfoModelSerializer(hero,many=True)
        hero_dict = hero_serializer.data

        #响应
        return Response(hero_dict)

    def delete(self,requesk,pk):
        #查询
        try:
            hero=HerroInfo.objects.get(pk=pk)
        except:
            return Response({'mag':'查询对象失败'})

        hero.delete()
        return Response(status=204)