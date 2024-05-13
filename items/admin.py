from django.contrib import admin
from .models import Item

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "uds")
    search_fields = ("name", "uds", "place")
    list_filter = ("place",)

admin.site.register(Item, ItemAdmin)
