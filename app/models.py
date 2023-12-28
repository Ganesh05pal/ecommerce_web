from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
STATE_CHOICE=(
    ('madhya pradesh','MADHYA PRADESH'),('gujrat','GUJRAT'),('uttar pradesh','UTTAR PRADESH'),('maharastra','MAHARASTRA'),
    ('ANDMAN & NICOBAR','ANDMAN & NICOBAR'),
    ('AANDHRA PRADESH','AANDHRA PRADESH'),

    ('BIHAR','BIHAR'),

    ('RAJISHTAN','RAJISHTAN'),

    ('DELHI','DELHI'),

    ('GOA','GOA'),
    ('ASSAM','ASSAM'),
    ('ARUNACHAL PRADESH','ARUNACHAL PRADESH'),
    

)

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    lacality=models.CharField( max_length=50)
    city=models.CharField(max_length=50)
    zip_code=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICE,max_length=50)

    def __str__(self):
        return str(self.id)

CATEGEROY_CHOICES=(
    ('M','MOBILE'),
    ('L','LAPTOP'),
    ('TW','TOP WEAR'),
    ('BW','BOTTOM WEAR')
)


class Product (models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    decription=models.TextField()
    brand=models.CharField(max_length=100)
    categroy=models.CharField(choices=CATEGEROY_CHOICES,max_length=2)
    Product_image=models.ImageField(upload_to='producting')
    


    def __str__(self):
        return str(self.id)
    
        
    
    
class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE )  
    quantity=models.PositiveBigIntegerField(default=1)

    
    def __str__(self):
        return str(self.id) 
    @ property
    def total_cost(self):
       return self.quantity * self.product.discounted_price    

STATUS_CHOICES=(
    ('accepted','accepted'),
    ('packed','packed'),
    ('On the way','on the way'),
    ('deliverd','delivered'),
    ('cencel','cencel')
)     
    
class OrderedPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)
    order_date=models.DateField(auto_now_add=True) 
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default="pending")
    
    def __str__(self) :
        return str(self.id)
    @ property
    def total_cost(self):
       return self.quantity * self.product.discounted_price 
        


    