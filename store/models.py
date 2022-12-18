from django.db import models

# Create your models here.
import datetime
import os

class Usersignup(models.Model):
    name = models.CharField(max_length=80)
    contactnum = models.CharField(max_length=12)
    postadress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    password = models.CharField(max_length=32)
    

class user_contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=70)
    massage=models.TextField(max_length=500)
    
def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('store/static/img', filename)
    
    
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50,null=True)
    category=models.CharField(max_length=50,default="",null=True)
    price=models.IntegerField(default=0,null=True)
    desc=models.TextField(max_length=500,null=True)
    pub_date=models.DateField(null=True)
    image=models.ImageField(upload_to=filepath,null=True, blank=True)
    
class Order(models.Model):
    name =models.CharField(max_length=70)
    cnum =models.IntegerField(max_length=14)
    pstad =models.CharField(max_length=50)
    city =models.CharField(max_length=50)
    payment =models.CharField(max_length=30)
    
def ConfirmOrderImagePath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('store/static/confirm', filename) 
   
        
class Cart(models.Model):
    image=models.ImageField(upload_to=ConfirmOrderImagePath,null=True, blank=True)
    product_name=models.CharField(max_length=50,null=True)
    desc=models.TextField(max_length=500,null=True)
    price=models.IntegerField(default=0,null=True)
    
def Soleditems(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('store/static/soled', filename)     
 
class Soled_item(models.Model):
    image=models.ImageField(upload_to=Soleditems,null=True, blank=True)
    product_name=models.CharField(max_length=50,null=True)
    desc=models.TextField(max_length=500,null=True)
    price=models.IntegerField(default=0,null=True)    