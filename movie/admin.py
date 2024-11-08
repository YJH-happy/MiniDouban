from django.contrib import admin
# Register your models here.
from .models import Movie,Review
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description')
    search_fields = ['title', 'description']
    list_editable = ('description',)

admin.site.register(Movie,MovieAdmin)
admin.site.register(Review)
