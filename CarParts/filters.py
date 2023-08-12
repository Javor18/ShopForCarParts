import django_filters
from .models import Tyre

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Tyre
        fields = ['brand', 'price']  # Filter by name and price