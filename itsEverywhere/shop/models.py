from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    category = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=350)
    publish_date = models.DateTimeField()
    product_image = models.ImageField(upload_to = 'shop/Images',default = '')

    def __str__(self):
        return self.product_name