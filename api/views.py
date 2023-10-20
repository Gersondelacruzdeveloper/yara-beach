from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'users':'api/users/',
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