from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('',views.home,name='home'),
    path('signup/',views.sign_up,name='signup'),
    path('signin/',views.sign_in,name='signin'),
    path('logout/',views.user_logout,name='logout'),
    
    path('cart/',views.cart,name='cart'),
    
    path('dashboard/',views.dashboard,name='dashboard'),
    path('contact/',views.contact,name='contact'),
    path('additem/',views.additem,name='additem'),
    path('updateitem/<int:id>/',views.updateitem,name='updateitem'),
    path('delitem/<int:id>/',views.delitem,name='delitem'),
    
    path('ConfirmOrder/',views.ConfirmOrder,name='ConfirmOrder'),
    
    path('soled/',views.soleditems,name='soled'),
    
    path('addtobuy/<int:id>/',views.addtobuy,name='addtobuy'),
    
    path('about/',views.about,name='about'),
    path('userrequest/',views.userrequest,name='userrequest'),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)