from django.urls import path
from .views import ProductList, ProductCreate, ProductUpdate, ProductDelete

urlpatterns = [
    path('home/', ProductList.as_view(), name='api-home'),
    path('create/', ProductCreate.as_view(), name='api-create'),
    path('<id>/update/', ProductUpdate.as_view(), name='api-update'),
    path('<id>/delete/', ProductDelete.as_view(), name='api-delete'),
]