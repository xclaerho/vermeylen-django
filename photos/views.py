from django.shortcuts import render
from photologue.models import Gallery, Photo
from django.views.generic import ListView, DetailView

class GalleryListView(ListView):
    model = Gallery
    queryset = Gallery.objects.filter(is_public=True)
    paginate_by = 3
    # custom template instead of photologue template
    template_name = 'photos/gallery_list.html'

class GalleryDetailView(DetailView):
    model = Gallery
    template_name = 'photos/gallery_detail.html'
