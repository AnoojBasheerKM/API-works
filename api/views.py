from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.views import APIView

from api.models import Lead

from api.serializers import LeadSerializer



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
    
    
class LeadistCreateView(APIView):
    
    def get(self,request,*args,**kwargs):
        
        qs = Lead.objects.all()

        serializer_instance = LeadSerializer(qs,many = True)

        return Response(data=serializer_instance.data)

    def post(self,request,*args,**kwargs):
        
        
        serializer_instance = LeadSerializer(data=request.data)

        if serializer_instance.is_valid():
            
            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        return Response(data=serializer_instance.errors)