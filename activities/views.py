from django.shortcuts import render, get_object_or_404
from .models import Activity
from datetime import datetime
# Create your views here.
def index(request):
    activities = Activity.objects.filter(start__gte=datetime.today()).order_by('start')
    context = {'activities': activities}
    return render(request, 'activities/index.html', context)

def detail(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    return render(request, 'activities/detail.html', {'activity': activity})