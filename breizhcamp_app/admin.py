from django.contrib import admin
from .models import Release, Genre, Artist, Song
# Register your models here.

admin.site.register(Release)
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Song)



