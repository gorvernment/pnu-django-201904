from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView
from .models import Item, Shop
from .forms import ShopForm, ItemForm

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
    query = request.GET.get('query', '').strip()    #query = request.GET['query']
    qs = Shop.objects.all()  # QuerySet 타입
    # print(query)

    if query:
        qs = qs.filter(name__icontains=query)

    # 템플릿 파일 위치 : shop/templates/shop/item_list.html
    return render(request, 'shop/shop_list.html', {
        'shop_list': qs,
        'query' : query,
    })

# shop_list = ListView.as_view(model=Shop, paginate_by=10)

def shop_detail(request, pk):
    shop = Shop.objects.get(pk=pk)
    return render(request, 'shop/shop_detail.html', {
        'shop' : shop,
    })

#shop_detail = DetailView.as_view(model=Shop)

def shop_new(request):
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/shop/')
    else:
        form = ShopForm()
    return render(request, 'shop/shop_form.html', {
        'form' : form,
    })

# shop_new = CreateView.as_view(model=Shop, form_class=ShopForm,
#                               success_url='/shop/')

def shop_edit(request, pk):
    shop = Shop.objects.get(pk=pk)

    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            form.save()
            return redirect('/shop/')
    else:
        form = ShopForm(instance=shop)
    return render(request, 'shop/shop_form.html', {
        'form' : form,
    })


def item_new(request):
    if request.method == 'GET':
        form = ItemForm()
    else:
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/shop/items/')
    return render(request, 'shop/item_form.html', {
        'form' : form,
    })
