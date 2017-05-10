from django.conf.urls import url
from django.views.generic import RedirectView

from .views import CategoryListView, ProductListView, ProductDetailView

urlpatterns = [
    url(r'^$',
        RedirectView.as_view(pattern_name='home')),
    url(r'^products/$',
        CategoryListView.as_view(), name='home'),
    url(r'^products/(?P<category_slug>[\w-]+)/$',
        ProductListView.as_view(), name='category'),
    url(r'^products/(?P<category_slug>[\w-]+)/(?P<product_slug>[\w-]+)$',
        ProductDetailView.as_view(), name='product')
]
