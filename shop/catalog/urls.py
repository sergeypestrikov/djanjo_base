from django.urls import path
from .views import ProductListView, AboutView, IndexView, CategoryListView

app_name = 'catalog'

urlpatterns = [
    path('catalog/', ProductListView.as_view(), name='catalog'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('about/', AboutView.as_view(), name='about'),
    path('', IndexView.as_view(), name='index'),
]