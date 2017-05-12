
from django.conf.urls import url
from django.views.generic import RedirectView

from .views import (
    CategoryListView,
    ProductListView,
    ProductDetailView,
#    Product24ListView
)

urlpatterns = [
    # If url is /, it will be redirected to products/
    url(r'^$',
        RedirectView.as_view(pattern_name='home')),
    url(r'^products/$',
        CategoryListView.as_view(), name='home'),

    # for accesing the page with products for the 24 hours
    url(r'^(?P<extra>[\w_]+)/$',
        ProductListView.as_view(), name='product_24'),
    
    url(r'^products/(?P<category_slug>[\w-]+)/$',
        ProductListView.as_view(), name='category'),
    url(r'^products/(?P<category_slug>[\w-]+)/(?P<product_slug>[\w-]+)$',
        ProductDetailView.as_view(), name='product'),
]
