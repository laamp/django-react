from django.contrib import admin
from .models import Collection


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'animation_speed', 'completed')


# Register your models here.
admin.site.register(Collection, CollectionAdmin)
