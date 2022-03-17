from django.contrib import admin

# Register your models here.
from .models import Product, Contact, Registration, checkoutPage, Order

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Registration)
admin.site.register(checkoutPage)
admin.site.register(Order)