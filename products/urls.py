from django.urls import path

# from rest_framework.authtoken.views import obtain_auth_token 

from .views import ProductList, ProductCreate, ProductUpdate, ProductDelete, ProductCreateMany, ProductDetail

urlpatterns = [
    path('home/', ProductList.as_view(), name='api-home'),
    path('<id>/detail', ProductDetail.as_view(), name='api-detail'),
    path('create/', ProductCreate.as_view(), name='api-create'),
    path('create/many', ProductCreateMany.as_view(), name='api-create-many'),
    path('<id>/update/', ProductUpdate.as_view(), name='api-update'),
    path('<id>/delete/', ProductDelete.as_view(), name='api-delete'),
    # path('auth/login/', obtain_auth_token, name='api-token'),
]