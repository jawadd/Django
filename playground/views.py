from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from store.models import Product
# Create your views here.


def hello(request):
    # does not require try and catch , as it will
    # return result or none
    # the .exists() return true or false
    # product = Product.objects.filter(pk=0).first()

    # product = Product.objects.filter(unit_aprice__range=(20, 30))
    # queryset = Product.objects.filter(unit_aprice__range=(20, 30))
    # queryset = Product.objects.filter(title__icontains='coffee')
    # combining conditions
    # queryset = Product.objects.filter(inventory__lt=10, unit_aprice__lt=20)
    # or we can also write
    # queryset = Product.objects.filter(
    #     inventory__lt=10).filter(unit_aprice__lt=30)

    # for using the OR we need to import Q as above and modify the queryset accordingly
    queryset = Product.objects.filter(
        Q(inventory__lt=20) | Q(unit_aprice__lt=20))

    return render(request, 'hello.html', {'name': 'Jawad', 'products': list(queryset)})
