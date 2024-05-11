from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.contrib.contenttypes.models import ContentType

from store.models import Product
from tags.models import TaggedItem
# Create your views here.


def hello(request):
    query_set = Product.objects.all()
    return render(request, "hello.html", {'products': query_set})

   #  product=Product.objects.get(pk=1)
   # the pk is auto translated into the required pk of the table by django
   # for the above line we weill require try and catch blocks in order to handle object does not exist
   # cases and we will require from django.core.exceptions import ObjectDoesNotExist
   # then
   # try:
   #     product=Product.objects.get(pk=1)
   # except ObjectDoesNotExist:
   #     pass
   # In Comparision exists=Product.objects.filter(pk=0).first does not require try and catch , as it will
   # return result or none
   # the .exists() return true or false
   # product = Product.objects.filter(pk=0).first()

    # Filtering Results google queryset api django and then field lookups
#     queryset=Product.objects.filter(unit_price__lt=20)
# #    queryset = Product.objects.filter(unit_price__range=(20, 30))
#     return render(request, "filtering.html", {'products': list(queryset)})
   # queryset = Product.objects.filter(unit_aprice__range=(20, 30))
#    case insensetive search
   # queryset = Product.objects.filter(title__icontains='coffee')
   # queryset = Product.objects.filter(title__startswith, endswith etc='coffee')
   # combining conditions
   # queryset = Product.objects.filter(inventory__lt=10, unit_aprice__lt=20)
   # or we can also write
   # queryset = Product.objects.filter(
   #     inventory__lt=10).filter(unit_aprice__lt=30)

   # for using the OR we need to import Q as above and modify the queryset accordingly
   # queryset = Product.objects.filter(
   # Q(inventory__lt=20) | Q(unit_price__lt=20))
   # to compare two different fields
   # queryset = Product.objects.filter(inventory=F('unit_price'))
   # we can also reference field of a related table
   #  queryset = Product.objects.filter(inventory=F('collection__id'))
   # Product.objects.order_by('title') , sorts by ascending
   #   #Product.objects.order_by('-title') , sorts by descending
   # .earliest() ascending, .latest('unit_price') descending
   # below two are the same , they return single result and not a queryset
   # product = Product.objects.latest('unit_price')
   #  product= Product.objects.order_by('unit_price')[0]
   # TaggedItem.objects.get_tags_for(Product, 1)
