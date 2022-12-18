from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from .forms import SignUpForm,SignInForm
from django.contrib.auth.forms import AuthenticationForm
# from .forms import SignUpForm,SignInForm,PostForm
from django.contrib.auth import authenticate,login,logout #for login
from .models import Usersignup,user_contact,Product,Order,Cart,Soled_item
# Create your views here.
import os
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
def home(request):
    products=Product.objects.all()
    
    return render(request,'store/home.html',{'products':products,'name':request.user.username})

def additem(request):
    if request.user.is_authenticated:
        if request.method=='POST': 
            pro=Product()
            pro.product_name=request.POST.get('product_name')
            pro.category=request.POST.get('category')
            pro.price=request.POST.get('price')
            pro.desc=request.POST.get('desc')
            pro.pub_date=request.POST.get('pub_date')
            
            if len(request.FILES)!=0:
                pro.image=request.FILES['image']

            # pst=Product(product_name=product_name,category=category,price=price,desc=desc,pub_date=pub_date,image=img)
            pro.save()
            messages.success(request, 'Item Added Sueccssfuly!')
            return render(request,'store/additem.html')
                
        else:
            return render(request,'store/additem.html')
    else:
        return HttpResponseRedirect('/signin/')

def updateitem(request,id):
    if request.user.is_authenticated:
        itm=Product.objects.get(id=id)
        if request.method=='POST':
            if len(request.FILES)!=0:
                if len(itm.image)>0:
                    os.remove(itm.image.path)
                itm.image=request.FILES['image']
            itm.product_name=request.POST.get('product_name')
            itm.category=request.POST.get('category')
            itm.price=request.POST.get('price')
            itm.desc=request.POST.get('desc')
            itm.pub_date=request.POST.get('pub_date')
            itm.save()
            messages.success(request, 'Updated Sueccssfuly!')
            return HttpResponseRedirect('/dashboard/')
  
        return render(request,'store/updateitem.html',{'items':itm})
    else:
        return HttpResponseRedirect('/signin/')
def delitem(request,id):
    if request.user.is_authenticated:
        itm=Product.objects.get(id=id)
        itm.delete()
        messages.success(request, 'Deleted Sueccssfuly!')
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/signin/')       
    
 
def about(request):
    return render(request,'store/about.html') 
 
def userrequest(request):
    req=Usersignup.objects.all()
    return render(request,'store/userrequest.html',{'reqts':req}) 



# SignUp using django UserCreationForm
def sign_up(request):
    if request.method=='POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            user=fm.save()
            group=Group.objects.get(name='User')
            user.groups.add(group)
            messages.info(request,'Signup Successfully!')
            fm=Product.objects.all()
            return render(request,'store/home.html',{'products':fm,'name':request.user.username})  
     
    else:
        fm=SignUpForm()
    return render(request,'store/signup.html',{'form':fm})
    
    
def sign_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignInForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                print(uname)
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    
                    login(request,user)
                    messages.success(request, 'Logged in Sueccssfuly!')
                    fm=Product.objects.all()
                    return render(request,'store/home.html',{'products':fm,'name':request.user.username})  
        else:
            fm= SignInForm()
        return render(request,'store/signin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/products/')
 
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
     

def cart(request):
    ck=Cart.objects.all()
    total=0
    for c in ck:
        total=total+c.price
    print(total)    
   
    return render(request,'store/order.html',{'products':ck,'tprice':total})  


def dashboard(request):
    if request.user.is_authenticated:
        order=len(Order.objects.all())
    
        if request.user.is_superuser == True:
            products=Product.objects.all().order_by('id')
            paginator=Paginator(products,3,orphans=1)
            page_number= request.GET.get('page')
            product_page = paginator.get_page(page_number)
            
            return render(request,'store/dashboard.html',{'products':product_page,'total':order})
           
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/signin/')


#contect model data saveing function
def addtobuy(request,id):
    if request.user.is_authenticated:
        itm=Product.objects.get(id=id)
        tobuy=Cart(image=itm.image,product_name=itm.product_name,desc=itm.desc,price=itm.price)
        tobuy.save()
        return HttpResponseRedirect('/') 
        
        
    else:
        messages.success(request, 'Please Login first!')
        return HttpResponseRedirect('/signin/')    
    


def ConfirmOrder(request):
    if request.method =='POST':
        name=request.POST.get('name')
        cnum=request.POST.get('cnum')
        pstad=request.POST.get('pstad')
        city=request.POST.get('city')
        payment=request.POST.get('payment')
        cn=Order(name=name,cnum=cnum,pstad=pstad,city=city,payment=payment)
        cn.save()
        cart=Cart.objects.all()
        
        for c in cart:
            soled=Soled_item(image=c.image,product_name=c.product_name,desc=c.desc,price=c.price)
            soled.save()
        Cart.objects.all().delete()
        
        messages.success(request, 'Oredr Conformed Shoping more!')
        return HttpResponseRedirect('/') 
    
 
def soleditems(request):
    soled=Soled_item.objects.all()
    byr=Order.objects.all() 
    return render(request,'store/soled.html',{'products':soled,'buyers':byr})    
    


def contact(request):
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        massage=request.POST.get('desc')
        cn=user_contact(name=name,email=email,phone=phone,massage=massage)
        cn.save()
        messages.success(request, 'Massage Sent!')
        return render(request,'store/contact.html') 
    return render(request,'store/contact.html')       