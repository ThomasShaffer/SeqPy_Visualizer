from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dna
from .serializers import DnaSerializer
from seqpy_library.SourceCode.dna import *

def index(request):
    return getRoutes(request)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
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
        },
        {
           'Endpoint': '/dna/id/delete',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes dna with the given primary key' 
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

@api_view(['PUT'])
def updateDna(request, primary_key):
    name, sequence = str(request.body,'utf-8').split(',')
    dna = Dna.objects.get(id=primary_key)
    dna.update(name, sequence)

    return Response("202")

@api_view(['GET'])
def computeDna(request, primary_key, computation):
    pre_dna = Dna.objects.get(id=primary_key)
    try: 
        computedDna = pre_dna.compute(computation)
        return Response(computedDna)
    except Exception as e:
        return Response(str(e))

@api_view(["DELETE"])
def deleteDna(request, primary_key):
    dna = Dna.objects.get(id=primary_key)
    dna.delete()
    return Response("deleted")


@api_view(["POST"])
def createDna(request):
    given_name, given_dna = str(request.body, 'utf-8').split(",")
    dna = Dna.objects.create(name=given_name, sequence=given_dna)
    return Response("created")