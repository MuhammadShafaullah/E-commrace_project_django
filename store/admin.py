from django.contrib import admin
from .models import Usersignup,user_contact,Product,Order,Cart,Soled_item
# Register your models here.


@admin.register(Usersignup)
class UsersignupAdmin(admin.ModelAdmin):
    list_display=('id','name','contactnum','postadress','city','password')
    
@admin.register(user_contact)
class user_contact(admin.ModelAdmin):
    list_display=('name','email','phone','massage')    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('product_id','product_name','category','price','desc','pub_date','image')  
  
@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display=('name','cnum','pstad','pstad','city','payment')      
    
@admin.register(Cart)
class item_cart(admin.ModelAdmin):
    list_display = ('id','product_name','desc','price','image')


@admin.register(Soled_item)
class Soled(admin.ModelAdmin):
    list_display = ('id','product_name','desc','price','image')
    
           
        