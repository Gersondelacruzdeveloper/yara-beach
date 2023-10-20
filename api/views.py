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
		'Task List for users':'api/task-list/?user_id="userId',
		'Message':'message/',
		'Group Mssage/':'api/group-message/',
		'call/':'api/call/',
		'voice-recognition':'api/voice-recognition/',
        'Face Recognition':'api/face-recognition',
        'Atatus':'api/status',
        'Status Media':'api/status-media',
        'screen Sharing session':'api/screen-sharing-session',
        'Streamingn Session/':'api/streaming_session/',
        'connected_users/':'api/connected_users/'
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

