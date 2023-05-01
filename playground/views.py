from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product
# Create your views here.


def hello(request):
    try:
        product = Product.objects.get(pk=0)
    except ObjectDoesNotExist:
        pass

    return render(request, 'hello.html', {'name': 'Jawad'})
