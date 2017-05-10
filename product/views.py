from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product
# Create your views here.


class CategoryListView(ListView):

    model = Category
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Home'
        # print(context)
        return context


class ProductListView(ListView):

    model = Product
    template_name = "category.html"

    def get_queryset(self):
        # print(self.kwargs)
        return Product.objects.all().filter(category=Category.objects.get(slug=self.kwargs['category_slug']))

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Category'
        # print(context)
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "product.html"
    slug_url_kwarg = "product_slug"


    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['title'] = self.object
        print(context)
        return context
