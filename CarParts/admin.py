from django.contrib import admin

# Register your models here.

from CarParts.models import Tyre

class TyreAdmin(admin.ModelAdmin):
    # list_display = ('id', 'name', 'price', 'brand', 'width', 'profile', 'rim', 'image', 'created_at', 'updated_at')
    # list_display_links = ('id', 'name')
    # list_filter = ('brand', 'width', 'profile', 'rim')
    # list_editable = ('price', 'image')
    # search_fields = ('name', 'brand', 'width', 'profile', 'rim')
    # list_per_page = 25

    list_display = ["brand", "model", "price", "width", "height", "diameter"]

admin.site.register(Tyre)