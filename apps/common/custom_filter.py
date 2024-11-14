from django_filters.rest_framework import FilterSet, CharFilter
from apps.products.models import Product


class ProductFilter(FilterSet):
    category = CharFilter(field_name="category__name", lookup_expr="iexact")
    price = CharFilter(field_name="price", lookup_expr=['gte', 'lte'])

    class Meta:
        model = Product
        fields = ['category', 'price']
