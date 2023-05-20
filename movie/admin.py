from django.contrib import admin
from .models import *

# Register your models here.
class Media(admin.TabularInline):
    model = media

class genres(admin.TabularInline):
    model = Genres

class Keyword(admin.TabularInline):
    model = keyword

class Downloadlink(admin.TabularInline):
    model = downloadlink

class allseason_series(admin.TabularInline):
    model = All_season

class movie_Admin(admin.ModelAdmin):
    inlines = (Media,genres, Keyword,Downloadlink,allseason_series, )

admin.site.register(category)
admin.site.register(movie,movie_Admin)
admin.site.register(media)
admin.site.register(Genres)
admin.site.register(keyword)
admin.site.register(downloadlink)
admin.site.register(session)
