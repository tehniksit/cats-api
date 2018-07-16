from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

from cats_api.cats.models import Cat
from cats_api.api.serializers import CatsSerializer


@api_view(['GET', 'POST'])
def cats_list(request):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        tasks = Cat.objects.all()
        serializer = CatsSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CatsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def cat_detail(request, pk):
    """
    Get, udpate, or delete a specific task
    """    
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    try:
        cats = Cat.objects.get(pk=pk)
    except Cat.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CatsSerializer(cats)
        return Response(serializer.data)
           

    elif request.method == 'PUT':
        serializer = CatsSerializer(cats, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cats.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

