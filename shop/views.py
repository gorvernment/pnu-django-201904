# from django.views.generic import ListView
from django.shortcuts import render
from .models import Item, Shop


# item_list = ListView.as_view(model=Item)


def item_list(request):
    # DB로부터 모든 Item List를 가져올 예정
    qs = Item.objects.all()  # QuerySet 타입
    # 템플릿 파일 위치 : shop/templates/shop/item_list.html
    return render(request, 'shop/item_list.html', {
        'item_list': qs,
    })


def item_detail(request, pk):
    item = Item.objects.get(pk=pk)  # 즉시 DB로부터 Fetch
    return render(request, 'shop/item_detail.html', {
        'item': item,
    })

def shop_list(request):
    qs = Shop.objects.all()  # QuerySet 타입
    # 템플릿 파일 위치 : shop/templates/shop/item_list.html
    return render(request, 'shop/shop_list.html', {
        'shop_list': qs,
    })
