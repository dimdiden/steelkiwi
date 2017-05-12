from datetime import datetime, timedelta

from django.views.generic import ListView, DetailView
from .models import Category, Product


# Display list of Categories
class CategoryListView(ListView):
    model = Category
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


# Display list of Products by specific Category
class ProductListView(ListView):
    model = Product
    template_name = "category.html"

    def get_queryset(self):
        """
        If an extra key is passed, the specific page is displayed.
        Otherwise - give the list of products groupped by the category
        based on the category_slug.
        """
        if 'extra' in self.kwargs and self.kwargs['extra'] == 'last_24_hours':
            last_24_hours = datetime.today() - timedelta(days=1)
            return Product.objects.all().filter(created_at__gte=last_24_hours)
        else:
            return Product.objects.all().filter(
                category=Category.objects.get(slug=self.kwargs['category_slug']))

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Category'
        return context


# Display detailed page for the specific Product
class ProductDetailView(DetailView):
    model = Product
    template_name = "product.html"
    slug_url_kwarg = "product_slug"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['title'] = self.object
        return context

