from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Client
from .serializers import ClientSerializer


@api_view(['GET'])
def index(request):
    api_urls = {
        'list': '/all/',
        'create': '/create/'
    }
    return Response(api_urls)


@api_view(['GET'])
def clientsList(request):
    clients = Client.objects.all().order_by('-id')
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createClient(request):
    serializer = ClientSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
