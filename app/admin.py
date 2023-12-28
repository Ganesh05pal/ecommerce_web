from django.contrib import admin
from .models import (
    Customer,
    Product,
    Cart,
    OrderedPlaced
)

# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    List_Display=['id','user','name','lacality','city','zip_code','state']
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    List_Display=['id','user''title','selling_price','discounted_price','desciption','brand','categroy','product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
   List_Display=['id','user','product','quantity']
@admin.register(OrderedPlaced)
class OrderplacedModelAdmin(admin.ModelAdmin):
    List_Display=['id','user','customer','quantity','order_date','prooduct','status']


