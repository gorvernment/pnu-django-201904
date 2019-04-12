from django.urls import path
from .views import item_list, item_detail, shop_list

app_name = 'shop'

urlpatterns = [
    path('', item_list),
    path('<int:pk>/', item_detail),
    path('shop_list/', shop_list),
]
