from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Registration, Order
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
# For Login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

import json

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
    # print(myProducts)

    prodCategory = []
    productsCat = Product.objects.values('category')
    # print(productsCat)
    # for item in productsCat:
    #     print(item["category"])
    categories = {item["category"] for item in productsCat}
    # print(categories)
    for cats in categories:
        # print(cats)
        catItems = Product.objects.filter(category = cats)
        productsCount = len(catItems)
        print("FIRST",catItems)
        # print(productsCount)
        prodCategory.append([catItems, range(0,productsCount)])
    # print(prodCategory)
    param = {"no_of_slides" : slides, "product" : myProducts, "range_for_slides" : range(0,slides), "prodCat" : prodCategory, "productsCount": range(0,productsCount)}
    return render(request,'shop/shopIndex.html',param)

def addToCart(request):
    return HttpResponse("HELLO ATC")

def product(request, id):
    # Filter and get particular product by id
    myProduct = Product.objects.filter(id=id)
    # print(myProduct)
    # print(myProduct[0])  #Because there will be only one product of this id which will be on "0" place
    return render(request, "shop/productView.html", {"product":myProduct[0]})

# Contact US
def contact(request):
    # print(request)
    if request.method == "POST":
        name = request.POST.get('name','')#First Parameter is "name" of our form. Second is for default value if given name is not found in form
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('description','')
        ourContact = Contact(name=name, email=email, phone=phone,desc=desc)
        ourContact.save()
    return render(request,"shop/contact.html")


class RegistrationAPI(APIView):
    def get(self,request):
        registerQueryset = Registration.objects.all()
        # print("MYGET")
        # print(registerQueryset)
        serializer = RegistrationSerializer(registerQueryset, many=True)

        return Response({"status":200, "payload":serializer.data})

    def post(self,request):
        registerData = request.data
        # print(registerData)
        mySerializer = RegistrationSerializer(data = request.data)
        if not mySerializer.is_valid():
            return Response({"status":403, "errors":mySerializer.errors,"message":"Something went wrong."})
        # mySerializer.set_password(mySerializer.password)
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        # print("MYPOST")
        myUser = User.objects.create_user(username,email,password)
        myUser.save()
        return Response({"status":200, "payload":registerData,"message":"Data has been registred."})

def checkout(request):
    if request.method == "POST":
        checkoutItems = request.POST.get('allCheckoutItems','')
        dct = json.loads(checkoutItems)
        # print("SECOND",checkoutItems)
        # print("THIRD",dct)
    param = {"allCheckoutItems":dct}
    return render(request,"shop/checkout.html",param)

def placeOrder(request):
    if request.method == "POST":
        checkoutItems = request.POST.get('allCheckoutItems','')
        param = {"checkoutItems":checkoutItems}
        return render(request,"shop/placeOrderForm.html",param)
    else:
        return HttpResponse("404-Page not found")

class placeOrderAPI(APIView):
    def post(self,request):
        # registerData = request.data
        # print("YEAH",registerData)
        mySerializer = PlaceOrderSerializer(data = request.data)
        if mySerializer.is_valid():
            name = request.POST.get("name", "")
            address1 = request.POST.get("address1", "")
            address2 = request.POST.get("address2", "")
            city = request.POST.get("city", "")
            state = request.POST.get("state", "")
            zip = request.POST.get("zip", "")
            checkoutItems = request.POST.get('allCheckoutItems','')
            myOrder = Order(name=name,address1=address1, address2=address2, city=city,state=state,zip=zip,checkoutItems=checkoutItems)
            myOrder.save()

            thankyou = True
            orderId = myOrder.order_id
            param = {"checkoutItems":checkoutItems, "thankyou":thankyou, "orderId":orderId}
            return render(request,"shop/thankyou.html",param)
        else:
            return HttpResponse(mySerializer.errors)
            # return Response({"status":200, "payload":registerData,"message":"Data has been registred."})
