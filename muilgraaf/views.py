from django.shortcuts import render
from django.contrib.auth.decorators import login_required,permission_required
from django.db.models import Q
from .models import Person, Link
from .forms import PersonAddForm, LinkAddForm

@login_required
@permission_required('muilgraaf.view_muilgraaf', raise_exception=True)
def muilgraaf(request):
    if request.method == 'POST':
        # check whether its person or link
        if 'person' in request.POST:
            form = PersonAddForm(request.POST)
            if form.is_valid():
                person = form.save()
                person.created_by = request.user
                person.save()
        elif 'link' in request.POST:
            form = LinkAddForm(request.POST)
            if form.is_valid():
                link = form.save()
                link.created_by = request.user
                link.save()
    # always reload the page
    people = Person.objects.filter(Q(first_person__isnull=False) | Q(second_person__isnull=False)).distinct()
    links = Link.objects.all()
    person_form  = PersonAddForm()
    link_form = LinkAddForm()
    context = {'people':people, 'links':links, 'person_form': person_form, 'link_form': link_form}
    return render(request, 'muilgraaf/muilgraaf.html', context)