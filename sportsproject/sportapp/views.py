from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import *

# Create your views here.

def function(req):
    return render()
def login(req):
    if 'user' in req.session:
        return redirect(home)
    if req.method=='POST':
        name=req.POST['username']
        password=req.POST['password']
        print(name,password)
        data=authenticate(username=name,password=password)
        print(data)
        if data is not None:
            req.session['user']=name
            print("abc")

            auth_login(req,data)
            return redirect(home)
    return render(req,'login.html')
    
def home(req):
    if 'user' in req.session:
        a=Products.objects.all()
        return render(req,'home.html',{'a':a})
    else:
        return redirect(login)
def registration(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        data=User.objects.create_user(first_name=name,email=email,username=username,password=password)
        data.save()
    return render(request,'registration.html')
def contact_view(request):
    return render(request, 'contact.html')
    
def about_view(request):
    return render(request, 'about.html') 
def products_view(request):
    # Your logic here
    return render(request, 'products.html')



def logout(req):
    if 'user' in req.session:
        auth_logout(req)
        # del req.session
        req.session.flush()
        return redirect(login)
    else:
        return redirect(login)
   

def viewproduct(req,id):
    a=Products.objects.get(pk=id)
    user=User.objects.get(username=req.session['user'])
    try:
        d=cartitems.objects.get(product=a,user=user)
        return render(req,"viewproduct.html",{'a':a,'d':d})

    except:
        return render(req,"viewproduct.html",{'a':a})
def cartdisplay(req):
    user=User.objects.get(username=req.session['user'])
    b=cartitems.objects.filter(user=user)
    
    return render(req,"addtocart.html",{'b':b})

def addtocart(req,id):
    
    a=Products.objects.get(pk=id)
    print(a)
    user=User.objects.get(username=req.session['user'])
    quantity=1

    totalprice=quantity*a.price
    cartitems.objects.create(product=a, user=user, quantity=quantity, totalprice=totalprice)
    return redirect(cartdisplay)

def ingrement(req,id):
    f=cartitems.objects.get(pk=id)
    f.quantity+=1
    f.totalprice=f.quantity*f.product.price
 
    f.save()
    # for i in f:
    print(f.quantity)
    return redirect(cartdisplay)     

def degrement(req,id):
    g=cartitems.objects.get(pk=id)
    if g.quantity>1:
       g.quantity-=1
       g.totalprice=g.quantity*g.product.price
       g.save()
       print(g.quantity)

    

    return redirect(cartdisplay)   

def delete_cart(req,id):
    d=cartitems.objects.get(pk=id)
    d.delete()
    return redirect(cartdisplay)

def address_info(request,id,cid):
    if request.method=='POST':
        w=Products.objects.get(pk=id)
        user=User.objects.get(username=request.session['user'])    
        address = request.POST.get('address')
        phone_no = request.POST.get('phone_no')
        state = request.POST.get('state')
        pin_code = request.POST.get('pin_code')
        land_mark = request.POST.get('land_mark')
        f=cartitems.objects.get(pk=cid)
        w.stock-=f.quantity
        w.save()
        
        data=buy.objects.create(address=address,phno=phone_no,state=state,pincode=pin_code ,user=user,landmark=land_mark,quantity=f.quantity,price=f.totalprice,cartitems=f)
        data.save()
        return redirect(my_orders)

    return render(request, 'addressinfo.html')  
    


def delete(req,cid):
    d=cartitems.objects.get(pk=cid)
    d=delete()
    return redirect(cartdisplay)
 

def my_orders(request):
    
    user=User.objects.get(username=request.session['user'])
    b=buy.objects.filter(user=user)
    return render(request, 'myorders.html', {'b': b})
