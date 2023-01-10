from django.shortcuts import render
from .models import Topic
# Create your views here.
def index(request):
    """This will resolve the index request"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """This page will show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)