from django.shortcuts import render
from App.serializers import EbookSerializer,UserSerializer
from App.models import Ebook,User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.


class EbookCreate(generics.CreateAPIView):
    queryset2 = Ebook.objects.all()
    serializer_class = EbookSerializer

class EbookDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

class AllEbook(generics.ListAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['review']

# class UserCreate(generics.CreateAPIView):
#     queryset2 = User.objects.all()
#     serializer_class = UserSerializer

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Alluser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class Registeruser(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors,'message':'Some thing went wrong'})
        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        token_obj , _ = Token.objects.get_or_create(user=user)
        return Response({'status':200,'payload':serializer.data,'token':str(token_obj),'message':'your data is saved'})