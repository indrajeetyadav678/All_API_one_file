from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from .models import *
import io

# Create your views here.
# ======= Normal API without Using DRF  ==============

# @csrf_exempt
# def normalapi(request):
#     if request.method=='POST':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         Queryset_data=Productserializer(data=python_data)
#         if Queryset_data.is_valid():
#             Queryset_data.save()
#             res={'msg':'Data Created'}
#             json_msg=JSONRenderer().render(res)
#             return HttpResponse(json_msg, content_type='application/json')
#         json_msg=JSONRenderer().render(Queryset_data.errors)
#         return HttpResponse(json_msg, content_type='application/json')
    
#     elif request.method=='GET':
#         queryset_data = ProductModel.objects.all()
#         queryset_data = Productserializer(queryset_data, many=True)
#         print(queryset_data.data) 
#         json_data=JSONRenderer().render(queryset_data.data)
#         return HttpResponse(json_data, content_type='application/json')
    
#     elif request.method=='PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         # id = python_data['id']
#         Product_data = ProductModel.objects.get(id=id)
#         queryset_data = Productserializer(Product_data, data=python_data)
#         # queryset_data = Productserializer(Product_data, data=python_data, partial=True)
#         if queryset_data.is_valid():
#             queryset_data.save()
#             res={'msg':'Data is Updated Successfully !!'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(queryset_data.errors)
#         return HttpResponse(json_data, content_type='application/json')
    
#     elif request.method =='DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         if id:
#             Product_data =ProductModel.objects.get(id=id)
#             Product_data.delete()
#             res={'msg':'Data Deleted'}
#             return JsonResponse(res, safe=False)
#         else:
#             res = {'msg':'id not present in Database'}
#             return JsonResponse(res)

# ================ Class based API ===========================

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class Product_list(APIView):
    def get(self, request, format=None):
        queryset_data=ProductModel.objects.all()
        serializer = Productserializer(queryset_data, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer=Productserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data successfully created'}
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Product_detail(APIView):
    def get_object(self, pk):
        try:
            return ProductModel.objects.get(id=pk)
    
        except ProductModel.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        queryset_data=self.get_object(pk)
        serializer=Productserializer(queryset_data)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        queryset_data=self.get_object(pk)
        serializer=Productserializer(queryset_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errrors, status=status.HTTP_400_BAD_REQUEST)
    
    def delede(self, request, pk, format=None):
        queryset_data=self.get_object(pk)
        queryset_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




