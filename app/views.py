from django.shortcuts import render,redirect
from django.views import View
from .models import Customer,Product,Cart,OrderedPlaced
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# def home(request):
#  return render(request, 'app/home.html')


class ProductView(View):
    def get(self,request):
      topwear=Product.objects.filter(categroy='TW')
      bottomwear=Product.objects.filter(categroy='BW')
      laptop=Product.objects.filter(categroy='L')
      mobile=Product.objects.filter(categroy='M')
      return render(request,"app/home.html",{'topwear':topwear,'bottomwear':bottomwear,'laptop':laptop,'mobile':mobile})


class ProductDetailView(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        
        item_already_in_cart=False
        if request.user.is_authenticated:
           item_already_in_cart =Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()

        
        return render(request,'app/productdetail.html', {'product':product,'item_already_in_cart':item_already_in_cart})    




# def change_password(request):
#  return render(request, 'app/changepassword.html')
@login_required
def mobile(request, data=None):
    if data==None:
        mobiles=Product.objects.filter(categroy='M')
    elif data=='oppo' or data=='redmi' or data=='one plus' or data=='vivo':
        mobiles=Product.objects.filter(categroy='M').filter(brand=data) 
    elif data=='below':
        mobiles=Product.objects.filter(categroy='M').filter(discounted_price__lt=10000)      
    elif data=='above':
        mobiles=Product.objects.filter(categroy='M').filter(discounted_price__gt=10000)      
    
    return render(request, 'app/mobile.html', {'mobiles':mobiles})


@login_required
def laptop(request, data=None):
    if data==None:
        laptops=Product.objects.filter(categroy='L')
    elif data=='Hp' or data=='Dell' or data=='Lenovo' or data=='APPLE':
        laptops=Product.objects.filter(categroy='L').filter(brand=data) 
    elif data=='below':
        laptops=Product.objects.filter(categroy='L').filter(discounted_price__lt=50000)      
    elif data=='above':
        laptops=Product.objects.filter(categroy='L').filter(discounted_price__gt=50000)      
    
    return render(request, 'app/laptop.html', {'laptops':laptops})

@login_required
def topwear(request, data=None):
    if data==None:
        topwears=Product.objects.filter(categroy='TW')
    # elif data=='oppo' or data=='redmi' or data=='one plus' or data=='vivo':
    #     mobiles=Product.objects.filter(categroy='M').filter(brand=data) 
    elif data=='below':
        topwears=Product.objects.filter(categroy='TW').filter(discounted_price__lt=500)      
    elif data=='above':
        topwears=Product.objects.filter(categroy='TW').filter(discounted_price__gt=500)      
    
    return render(request, 'app/topwear.html', {'topwears':topwears})

@login_required
def bottomwear(request, data=None):
    if data==None:
        bottomwears=Product.objects.filter(categroy='BW')
    # elif data=='oppo' or data=='redmi' or data=='one plus' or data=='vivo':
    #     mobiles=Product.objects.filter(categroy='M').filter(brand=data) 
    elif data=='below':
        bottomwears=Product.objects.filter(categroy='BW').filter(discounted_price__lt=1000)      
    elif data=='above':
        bottomwears=Product.objects.filter(categroy='BW').filter(discounted_price__gt=1000) 
           
    
    return render(request, 'app/bottomwear.html', {'bottomwears':bottomwears})


def login(request):
 return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')
class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',{'form':form})
    def post(self,request):
        form =CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,"congratulations !! successfully registred ")
            form.save()
            
        return render(request,'app/customerregistration.html',{'form':form})
        



@method_decorator(login_required, name="dispatch")
class ProfileView(View):
 def get(self,request):
  form = CustomerProfileForm()

  return render(request, 'app/profile.html',{'form':form,'active':'btn-primary'})
 def post(self,request):
   form = CustomerProfileForm(request.POST)
   if form.is_valid():
     usr =request.user
     name =form.cleaned_data['name']
     lacality =form.cleaned_data['lacality']
     city =form.cleaned_data['city']
     state =form.cleaned_data['state']
     zip_code =form.cleaned_data['zip_code']
     reg = Customer (user=usr,name=name,lacality=lacality,city=city,state=state,zip_code=zip_code)
     reg.save()
     messages.success(request,"Congrulations!! profile Updated Succesfully ")
   return render(request, 'app/profile.html',{'form':form,'active':'btn-primary'})

def plus_cart(request):
   if request.method=='GET' :
      prod_id =request.GET["prod_id"] 
      print(prod_id)
      c =Cart.objects.get(Q(product=prod_id) & Q(user=request.user)) 
      c.quantity+=1
      c.save()
      amount=0.0
      shipping_amount=70.00
      cart_product=[p for p in Cart.objects.all() if p.user==request.user]
      for p in cart_product:
          tempamount =(p.quantity * p.product.discounted_price)
          amount += tempamount 
      data ={
        'quantity': c.quantity,
        'amount': amount,
        'totalamount':amount+shipping_amount
          }
      return JsonResponse(data)
def minus_cart(request):
   if request.method=='GET' :
      prod_id =request.GET["prod_id"] 
      print(prod_id)
      c =Cart.objects.get(Q(product=prod_id) & Q(user=request.user)) 
      c.quantity-=1
      c.save()
      amount=0.0
      shipping_amount=70.00
      cart_product=[p for p in Cart.objects.all() if p.user==request.user]
      for p in cart_product:
          tempamount =(p.quantity * p.product.discounted_price)
          amount += tempamount 
      data ={
        'quantity': c.quantity,
        'amount': amount,
        'totalamount':amount+shipping_amount
        }
      return JsonResponse(data)

def remove_cart(request):
    if request.method=='GET' :
      prod_id =request.GET["prod_id"] 
      print(prod_id)
      c =Cart.objects.get(Q(product=prod_id) & Q(user=request.user)) 
      c.delete()
      amount=0.0
      shipping_amount=70.00
      cart_product=[p for p in Cart.objects.all() if p.user==request.user]
      for p in cart_product:
          tempamount =(p.quantity * p.product.discounted_price)
          amount += tempamount 
      data ={
        'amount': amount,
        'totalamount':amount+shipping_amount
        }
      return JsonResponse(data)

@login_required
def checkout(request):
 user=request.user
 add =Customer.objects.filter(user=user)
 cart_items =Cart.objects.filter(user=user)
 amount=0.0
 shipping_amount=70.00
 cart_product=[p for p in Cart.objects.all() if p.user==request.user]
 if cart_product:
  for p in cart_product:
    tempamount =(p.quantity * p.product.discounted_price)
    amount += tempamount
    totalamount =amount+shipping_amount  
 return render(request, 'app/checkout.html',{'add':add,"totalamount":totalamount,'cart_items':cart_items})

@login_required
def payment_done(request):
    user=request.user
    custid=request.GET.get('custid')
    customer =Customer.objects.get(id=custid)
    cart=Cart.objects.filter(user=user)
    for c in cart:
       OrderedPlaced(user=user,customer=customer,
                     product=c.product,quantity=c.quantity).save()
       c.delete()
    return redirect('orders')

@login_required
def orders(request):
    op =OrderedPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html',{"order_placed":op})

@login_required
def add_to_cart(request):
 user = request.user
 product_id =request.GET.get('prod_id')
 product =Product.objects.get(id=product_id)
 store=Cart(user=user,product=product)
 store.save()
 return redirect('/cart')

@login_required
def show_cart(request):
   if request.user.is_authenticated:
    user =request.user
    cart =Cart.objects.filter(user=request.user)
    print(cart)
    amount=0.0
    shipping_amount =70.0
    total_amount =  0.0
    cart_product =[p for p in Cart.objects.all() if p.user==request.user]
    if cart_product:
        for p in cart_product:
          tempamount =(p.quantity * p.product.discounted_price)
          amount += tempamount 
          totalamount =amount+shipping_amount
        return render(request, 'app/addtocart.html',{'carts':cart , 'amount':amount , 'totalamount':totalamount})
    else:
       return render(request, 'app/emptycart.html')
    

        
def buy_now(request):
 return render(request, 'app/buynow.html')
@login_required
def address(request):
 add = Customer.objects.filter(user=request.user)
 return render(request, 'app/address.html',{'add':add ,'active':'btn-primary'})
