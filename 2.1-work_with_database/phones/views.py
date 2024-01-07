from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sorting = request.GET.get('sort')
    if sorting == 'name': phones = phones.order_by('name')
    if sorting == 'min_price': phones = phones.order_by('price')
    if sorting == 'max_price': phones = phones.order_by('price').reverse()

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
