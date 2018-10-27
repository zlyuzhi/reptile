from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from index.models import BookInfo, HerroInfo
# Create your views here.
from django.views import View


def first(request):
    return HttpResponse('Django')

def weather(request,city,year):

    url =reverse('index:first')
    return redirect(url)
    print('city=%s' % city)
    print(url)
    print('year=%s'% year)
    return HttpResponse('ok')

# class RegisterView(View):
#     def get(serlf,request):
#         return render(request,'register.html')
#     def post(self,request):
#         return HttpResponse('逻辑的实现')

class SelectView(View):
    def get(self,request):

        blist=[]
        try:
            blist=BookInfo.objects.get(pk=1)
            print(blist.btitle)
        except:
            print('查询失败')

        # return render(request,'index.html',{'blist':blist})
from .serializers import BookInfoSerializer,HerroInfoSerialize

class BookTestView(View):
    def get(self,request):
        # book = BookInfo.objects.get(pk=1)
        # serializer= BookInfoSerializer(book)
        # book_dict =serializer.data
        # return JsonResponse(book_dict)
        books =BookInfo.objects.all()
        serializer=BookInfoSerializer(books,many=True)
        book_dict =serializer.data
        return JsonResponse(book_dict,safe=False)

# class HeroTestView(View):
#     def get(self,request):
#         hero=HerroInfo.objects.get(pk=1)
#
#         serializer=HerroInfoSerialize(hero)
#         hero_dict=serializer.data

        # return JsonResponse(hero_dict)











