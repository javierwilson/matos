from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Operation
from .serializers import OperationSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def operation_list(request):
    """
    List all operations, or create a new operation.
    """
    if request.method == 'GET':
        operations = Operation.objects.all()
        serializer = OperationSerializer(operations, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid():
            #import pdb; pdb.set_trace()
            ip = request.META.get('REMOTE_ADDR')
            result = 0
            numbers = list(serializer.validated_data['numbers'])
            operation = serializer.validated_data['operation']
            if operation == 'suma':
                result = sum(numbers)
            if operation == 'add':
                result = sum(numbers)
            if operation == 'mult':
                result = reduce(lambda x, y: x*y, numbers)
            serializer.save(ip=ip, result=result)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def operation_detail(request, pk):
    """
    Retrieve, update or delete a operation instance.
    """
    try:
        operation = Operation.objects.get(pk=pk)
    except Operation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OperationSerializer(operation)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OperationSerializer(operation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        operation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
