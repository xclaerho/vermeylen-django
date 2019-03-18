from django.shortcuts import render
from .forms import InputForm
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bedankt voor de input!')
            form = InputForm()
        else:
            messages.warning(request, 'Er ging iets mis.')
    else:
        form = InputForm()
    context = {'form': form}
    return render(request, 'input/input.html', context)