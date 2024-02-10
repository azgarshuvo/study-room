from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer


@api_view(['GET']) # it can take ['GET', 'POST', 'PUT']
def getRoutes(request):
    routes = [
        'GET /api'
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes) # the JsonResponse method return a json list


@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True) # if there are many objects
    return Response(serializer.data)


@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False) # return back a single object
    return Response(serializer.data)


@api_view(['POST'])
def createRoom(request):
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(instance=room, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    room.delete()
    return Response('Task deleted successfully!')

