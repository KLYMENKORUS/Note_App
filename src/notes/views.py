from django.views.generic import ListView, DetailView
from .models import Category


class ListCategoriesView(ListView):
    model = Category
    template_name = 'index.html'


class DetailCategoriesView(DetailView):
    model = Category
    template_name = 'detail.html'
    context_object_name = 'category'


