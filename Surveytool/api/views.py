from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
import json

from .serializers import infoSerializers,questionSerializers
from .models import info,question


@api_view(["GET"])
@csrf_exempt
 
def welcome(request):
    content = {"message": "Welcome to Survey!"}   #startup page
    return JsonResponse(content)

@api_view(["GET"])                 # To view all users
def get_info(request):
    if request.method == 'GET':

          Info = info.objects.all()
          serializer = infoSerializers(Info, many=True)
          return JsonResponse({'info': serializer.data}, safe=False, status=status.HTTP_200_OK)
        
 #To add users
    elif request.method == 'POST':  
        

        serializer = infoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_question(request):               # To view all questions
    if request.method == 'GET':

          Info = question.objects.all()
          serializer = questionSerializers(Info, many=True)
          return JsonResponse({'Questions': serializer.data}, safe=False, status=status.HTTP_200_OK)



            
  