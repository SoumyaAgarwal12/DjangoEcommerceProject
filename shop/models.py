from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    category = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    price = models.IntegerField(default=0)
    publish_date = models.DateTimeField()
    product_image = models.ImageField(upload_to = 'shop/Images',default = '')

    def __str__(self):
        return self.product_name

# Create your models here.
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField(default=0)
    desc = models.CharField(max_length=1000)
    # publish_date = models.DateTimeField()

    def __str__(self):
        return self.name

class Registration(models.Model):
    reg_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=80)

    def __str__(self):
        return self.username

class checkoutPage(models.Model):    # OneToOneField experiment 
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    checkoutItems = models.CharField(max_length=50)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=1000)
    address2 = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    checkoutItems = models.CharField(max_length=100000,default="")

    def __str__(self):
        return self.name
