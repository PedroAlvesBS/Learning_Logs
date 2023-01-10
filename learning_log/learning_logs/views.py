from django.shortcuts import render

# Create your views here.
def index(request):
    """This will resolve the index request"""
    return render(request, 'learning_logs/index.html')