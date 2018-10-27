from django.shortcuts import render

# Create your views here.
# from requests import Response
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserCreateSerializer


class UsernameCountView(APIView):
    def get(self,request,username):
        count=User.objects.filter(username=username).count()
        return Response({'username':username,
                             'count':count
        })

class MobileCountView(APIView):
    def get(self,request,mobile):
        count=User.objects.filter(mobile=mobile).count()

        return Response({'mobile':mobile,
                             'count':count
            })

class UserCreateView(CreateAPIView):
    serializer_class =UserCreateSerializer