from django.contrib import admin
from django.http import HttpResponse
import csv

# Register your models here.

from CarParts.models import Tyre

class TyreAdmin(admin.ModelAdmin):

    list_display = ["brand", "model", "price", "width", "height", "diameter"]
    search_fields = ["brand", "model"]

    list_filter = ["brand"]

    ordering = ["-brand"]

    def export_csv_action(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')

        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)

        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_csv_action.short_description = "Export selected to CSV"
    actions = ["export_csv_action"]

admin.site.register(Tyre, TyreAdmin)