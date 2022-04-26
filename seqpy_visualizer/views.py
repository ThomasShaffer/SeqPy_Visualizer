from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dna
from .serializers import DnaSerializer
from seqpy_library.SourceCode.dna import *

def index(request):
    return getRoutes(request)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/',
            'method': 'GET',
            'body': None,
            'description': 'Returns all sequences' 
        },

        {
            'Endpoint': '/dna/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a DNA object'
        },

        {
            'Endpoint': '/dna/create',
            'method': 'POST',
            'body': None,
            'description': 'Creates new DNA object with parameters passed in'
        },

        {
            'Endpoint': '/dna/id/update',
            'method': 'PUT',
            'body': None,
            'description': 'Updates existing dna with parameters passed in'
        }
    ]
    return Response(request)

@api_view(['GET'])
def getDnas(request):
    all_dna = Dna.objects.all()
    serializer = DnaSerializer(all_dna, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDna(request, primary_key):
    dna = Dna.objects.get(id=primary_key)
    serializer = DnaSerializer(dna, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def updateDna(request, primary_key):
    data = request.data
    dna = Dna.objects.get(id=primary_key)
    serializer = DnaSerializer(instance=dna, data=data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#TODO: MUST CHANGE LOGIC IN VIEWS AND SEND IT TO MODELS.PY
@api_view(['GET'])
def computeDna(request, primary_key, computation):
    pre_dna = Dna.objects.get(id=primary_key)
    print(pre_dna)
    try: 
        computedDna = pre_dna.compute(computation)
        return Response(computedDna)
    except:
        Exception
        return Response("ERROR")

@api_view(["POST"])
def createDna(request, primary_key):
    return Response("idk")