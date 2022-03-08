from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Registration
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
# For Login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

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
        # print(catItems)
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
        print(desc)
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
        add1 = request.data['address1']
        add2 = request.data['address2']
        city_name = request.data['city']
        zip_code = request.data['zip']
        state_name = request.data['state']
        # print("MYPOST")
        myUser = User.objects.create_user(username,email,password)
        myUser.address1 = add1
        myUser.address2 = add2
        myUser.city_name = city_name
        myUser.city = zip_code
        myUser.state = state_name
        myUser.save()
        return Response({"status":200, "payload":registerData,"message":"Data has been registred."})


def loginPage(request):
    return HttpResponse("HELLO LOGINPAGE")