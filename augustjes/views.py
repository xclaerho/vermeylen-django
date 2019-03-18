from django.shortcuts import render
from django.views.generic import ListView, DetailView
from datetime import date
from .models import Augustje, Subscriber
from .forms import SubscriberForm
from django.contrib import messages

class AugustjeListView(ListView):
    queryset = Augustje.objects.filter(date__lte=date.today())

    def get(self, request):
        form = SubscriberForm()
        queryset = Augustje.objects.filter(date__lte=date.today())
        return render(request,'augustjes/augustje_list.html', {'form':form, 'object_list': queryset})

    def post(self, request):
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Antwoord opgeslagen')
            form = SubscriberForm()
        else:
            messages.warning(request, 'Er ging iets mis.')
        queryset = Augustje.objects.filter(date__lte=date.today())
        return render(request,'augustjes/augustje_list.html', {'form':form, 'object_list': queryset})

class AugustjeDetailView(DetailView):
    model = Augustje        