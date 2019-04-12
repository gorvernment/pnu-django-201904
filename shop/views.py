from django.shortcuts import render
from .models import Item, Shop

# Create your views here.
def item_list(request):
    qs = Item.objects.all()
    return render(request, 'shop/item_list.html', {
        'item_list' : qs,
    })

def item_detail(request, pk):
    item = Item.objects.get(pk=pk)
    return render(request, 'shop/item_detail.html', {
        'item' : item,
    })

def shop_list(request):
    qs = Shop.objects.all()  # QuerySet 타입
    # 템플릿 파일 위치 : shop/templates/shop/item_list.html
    return render(request, 'shop/shop_list.html', {
        'shop_list': qs,
    })


def shop_detail(request, pk):
    shop = Shop.objects.get(pk=pk)
    return render(request, 'shop/shop_detail.html', {
        'shop' : shop,
    })