from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
# def index(request):
#     return HttpResponse("HELLO SHop")

def index(request):
    myProducts = Product.objects.all()
    productsLength = len(myProducts)
    if(productsLength%3 == 0):
        slides = productsLength//3
    else:
        slides = productsLength//3  + 1
    print(myProducts)

    prodCategory = []
    productsCat = Product.objects.values('category')
    # print(productsCat)
    # for item in productsCat:
    #     print(item["category"])
    categories = {item["category"] for item in productsCat}
    # print(categories)
    print("SOUMYA")
    for cats in categories:
        # print(cats)
        catItems = Product.objects.filter(category = cats)
        productsCount = len(catItems)
        print(catItems)
        print(productsCount)
        prodCategory.append([catItems, range(0,productsCount)])
    print("AGARWAL")
    print(prodCategory)
    param = {"no_of_slides" : slides, "product" : myProducts, "range_for_slides" : range(0,slides), "prodCat" : prodCategory, "productsCount": range(0,productsCount)}
    return render(request,'shop/shopIndex.html',param)

def addToCart(request):
    return HttpResponse("HELLO ATC")