from django.shortcuts import render
from django.utils import timezone
from .models import Speed
from .forms import PostForm

# Create your views here.
def speed_list(request):
    speeds = Speed.objects.order_by('-Timestamp')
    return render(request, 'speed/speed_list.html', {'speeds': speeds})

def speed_new(request):
    #Speed.publish()
    Speed.publish   #objects.filter(Timestamp__lte=timezone.now()).order_by('Timestamp')
    speeds = Speed.objects.filter(Timestamp__lte=timezone.now()).order_by('-Timestamp')
    return render(request, 'speed/speed_list.html', {'speeds': speeds})

def speed_detail(request, pk):
    speed = get_object_or_404(Post, pk=pk)
    return render(request, 'speed/post_detail.html', {'speed': speed})