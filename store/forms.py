from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm #for creating user
from django.contrib.auth.forms import AuthenticationForm #for Login 
from django.contrib.auth.forms import UsernameField #for Login 
from django.utils.translation import gettext,gettext_lazy as _
from .models import Product

#SignUp UserCreationForm Custom form 
class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels= {'first_name':'First Name','last_name':'Last Name','email':'Email',}
        
        widgets={'username':forms.TextInput(attrs={'class':'form-control',}),
                'first_name':forms.TextInput(attrs={'class':'form-control'}),
                'last_name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.TextInput(attrs={'class':'form-control'})
        }
        
       
class SignInForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password=UsernameField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autofocus':True, 'class':'form-control'})) 
    
# class add_item(forms.ModelForm):
#     class Meta:
#         model = Product 
#         fields=['product_name','category','price','desc','pub_date','image']  
#         labels={'product_name':'Product Name','category':'Category','price':'Price','desc':'Description','pub_date':'Publish Date','image':'Image'}
       
#         widgets={'product_name':forms.CharField(),
#                  'category':forms.CharField(),
#                  'price':forms.IntegerField(),
#                  'desc':forms.Textarea(),
#                  'pub_date':forms.DateField(),
#                  'image':forms.ImageField(),
#                 }                