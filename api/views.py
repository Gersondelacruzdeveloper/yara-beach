from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TaskSerializer
from .models import Task
from django.http import Http404
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
        'Api overview': 'api',
		'Task List for users':'api/task-list/?user_id="userId',
		'Update Task':'api/task/<int:task_id>',
		}
	return Response(api_urls)


@api_view(['GET'])
def task_list(request):
    if request.method == 'GET':
        user_id = request.query_params.get('user_id')
        
        # Validate and sanitize the user_id
        try:
            user_id = int(user_id)  # Try to convert user_id to an integer
        except (ValueError, TypeError):
            return Response({'error': 'Invalid user_id'}, status=status.HTTP_400_BAD_REQUEST)
        
        if user_id is not None:
            try:
                user = User.objects.get(pk=user_id)
            except User.DoesNotExist:
                raise Http404("User does not exist")

            tasks = Task.objects.filter(user=user)
        else:
            tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



# all the models query here together
@api_view(['POST'])
def add_task(request):
    if request.method == "POST":
        data = request.data
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Task created successfully.", "data": serializer.data}, status=status.HTTP_201_CREATED)
        print('data', serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# update the task
@api_view(['PUT'])
def update_task(request, task_id):
    if request.method == 'PUT':
        try:
            task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            return Response({'error': 'Task does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # You can add further checks here to ensure the task belongs to the user if needed

        # Update the task with the new data
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Task updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)