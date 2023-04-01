from django.urls import path
from .views import ListCategoriesView, DetailCategoriesView

app_name = 'notes'

urlpatterns = [
    path('', ListCategoriesView.as_view(), name='index'),
    path('category/<int:pk>/', DetailCategoriesView.as_view(), name='detail')
]