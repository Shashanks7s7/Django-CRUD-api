
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import inputSerializer
from .models import input
import json
import difflib
from myapi import serializers

# Create your views here.

@api_view(['GET'])
def getdatas(request):
    notes=input.objects.all()
    serializer = inputSerializer(notes,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getdata(request,pk):
    note=input.objects.get(id=pk)
    serializer = inputSerializer(note,many=False)
    return Response(serializer.data)    

@api_view(['POST'])
def createdata(request):
    data=request.data

    note = input.objects.create(     
        title=data['title']
    )
    serializers=inputSerializer(note,many=False)     
    return Response(serializers.data)

@api_view(['PUT'])
def updatedata(request,pk):
    data = request.data   
    note= input.objects.get(id=pk)

    serializers=inputSerializer(note,data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE'])
def deletedata(request,pk):
    note=input.objects.get(id=pk)
    note.delete()
    return Response('Data was deleted')