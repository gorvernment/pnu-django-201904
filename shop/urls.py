from django.urls import path
#from .views import item_list, item_detail, shop_list, shop_detail, shop_new
from . import views

app_name = 'shop'

urlpatterns = [
    #path('', item_list),
    #path('new/', shop_new),
    #path('<int:pk>/', item_detail),
    #path('shop/', shop_list),
    #path('shop/<int:pk>/', shop_detail),

    path('', views.shop_list, name='shop_list'),
    path('new/', views.shop_new, name='shop_new'),
    path('<int:pk>/edit/', views.shop_edit, name='shop_edit'),
    path('<int:pk>/', views.shop_detail, name='shop_detail'),

    path('items/', views.item_list, name='item_list'),
    path('items/new/', views.item_new, name='item_new'),
    path('items/<int:pk>/', views.item_detail, name='item_detail'),
]
