from django.contrib import admin

from photologue.models import Gallery, Photo
from photologue.admin import GalleryAdmin as GalleryAdminDefault
from photologue.admin import PhotoAdmin as PhotoAdminDefault

class GalleryAdmin(GalleryAdminDefault):
    pass

class PhotoAdmin(PhotoAdminDefault):
    pass

admin.site.unregister(Gallery)
admin.site.register(Gallery, GalleryAdmin)
admin.site.unregister(Photo)
admin.site.register(Photo, PhotoAdmin)
