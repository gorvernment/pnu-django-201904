from django.urls import path
from .views import item_list, item_detail, shop_list, shop_detail

app_name = 'shop'

urlpatterns = [
    path('', item_list),
    path('<int:pk>/', item_detail),
    path('shop/', shop_list),
    path('shop/<int:pk>/', shop_detail),
]
