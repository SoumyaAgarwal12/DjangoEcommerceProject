from django.db import models

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