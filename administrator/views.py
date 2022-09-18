from django.shortcuts import render

# Create your views here.

# Administrator function
def administrator(request):
    context = {}
    return render(request, 'administrator/administrator.html', context)