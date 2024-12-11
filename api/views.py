from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.views import APIView


# Create your views here.

class BookCreateListView(APIView):
    
    def get(self,request,*args,**kwargs):
        
        context = {"message":"listing all books"}

        return Response(data=context)

    def post(self,request,*args,**kwargs):
        
        context = {"message":"creating a new book"}

        return Response(data=context)

class BookRetrieveUpdateDestroyView(APIView):
    
    def get(self,request,*args,**kwargs):
        
        context = {"message":"listing a specific book detail"}

        return Response(data=context)

    def put(self,request,*args,**kwargs):

        context = {"message":"updating a specific book"}

        return Response(data=context)

    def delete(self,request,*args,**kwargs):
        
        context = {"message":"Deleting a specific book"}

        return Response(data=context)