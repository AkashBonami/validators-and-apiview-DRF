from functools import partial
from django.shortcuts import render
from .models import *
from .serializers import *
import json
from django.http import HttpResponse 
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

class StudentAPI(APIView):
    def get(self,request):
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        # data = json.loads(request.body)
        serializer=StudentSerializer(data=request.data)    
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data saved'}
            json_data=JSONRenderer().render(res)
            return Response(json_data,content_type='application/json')
        else:
            json_data=serializer.errors
            return Response(json_data,content_type='application/json')
class StudentAPI1(APIView):
    def delete(self,request,id):
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response("Deleted")
    def put(self,request,id):
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def patch(self,request,id):
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)