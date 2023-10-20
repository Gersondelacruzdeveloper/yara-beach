from rest_framework import serializers
from .models import Task  # Import your Task model

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'  # You can specify the fields you want to include explicitly if needed

    # You can also add custom validation or methods to your serializer here if required
