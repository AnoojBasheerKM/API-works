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
    
class LeadCreateUpdateRetrieveDeleteView(APIView):
    
    serializer_class = LeadSerializer
    
    def get(self,request,*args,**kwargs):
        
        id = kwargs.get("pk")

        qs = Lead.objects.get(id=id)

        serializer_instance = self.serializer_class(qs)

        return Response(data=serializer_instance.data)
    
    def delete(self,request,*args,**kwargs):
        
        id = kwargs.get("pk")

        qs = Lead.objects.get(id=id).delete()

        return Response(data={"message":"deleted"})
    
    def put(self,request,*args,**kwargs):
        
        id = kwargs.get("pk")

        lead_object = Lead.objects.get(id=id)

        serializer_instance = self.serializer_class(data=request.data,instance=lead_object)

        if serializer_instance.is_valid():
            
            serializer_instance.save()

            return Response(data=serializer_instance.data)

        return Response(data=serializer_instance.errors)
    
from django.db.models import Count
class LeadSummaryView(APIView):
    
    def get(self,request,*args,**kwargs):
        
        total_lead_count = Lead.objects.all().count()
        
        source_summary = Lead.objects.all().values("source").annotate(count=Count("source"))
        
        enquiry_summary = Lead.objects.all().values("course").annotate(count=Count("course"))
        
        status_summary = Lead.objects.all().values("status").annotate(count=Count("status"))

        context={
            
            "total":total_lead_count,
            "source":source_summary,
            "course":enquiry_summary,
            "status":status_summary
        }
        
        return Response(data=context)

        