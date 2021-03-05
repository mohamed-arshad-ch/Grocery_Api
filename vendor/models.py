from django.db import models
from django.contrib.auth.models import AbstractUser
import math
import uuid
# Create your models here.

class CustomUser(AbstractUser):
    user_type = models.BooleanField(blank=False,null=False,default=True)
    company_name = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    year = models.CharField(max_length=100,null=True,blank=True)
    employees = models.CharField(max_length=100,null=True,blank=True)
    category = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    zipc = models.CharField(max_length=100,null=True,blank=True)


    def __str__(self):
        return self.username

class ChartOfAccounts(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    typeof = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ChartOfAccounts,on_delete=models.CASCADE,related_name="categorytype")
    active = models.BooleanField(default=True)



class Product(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    image = models.ImageField()
    category = models.ForeignKey(ChartOfAccounts,on_delete=models.SET_NULL,null=True,related_name='category')
    subcategory = models.ForeignKey(SubCategory,on_delete=models.SET_NULL,null=True,related_name='subcategory')
    tag = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    discount = models.IntegerField()
    tax = models.ForeignKey(ChartOfAccounts,on_delete=models.SET_NULL,null=True,related_name='tax')
    attr_type = models.IntegerField(null=True,blank=True)
    total_stock = models.IntegerField()
    available_stock = models.IntegerField()
    brand = models.ForeignKey(ChartOfAccounts,on_delete=models.SET_NULL,null=True,related_name='brand')
    unit = models.ForeignKey(ChartOfAccounts,on_delete=models.SET_NULL,null=True,related_name='unit')
    active = models.BooleanField(default=False)

    def with_tax_price(self):
        total = 0
        jk = (self.price * int(self.tax.name))/100
        total = self.price + jk
        return total

    

    def get_total(self):

        total = 0
        
        ip = (self.price * self.discount)/100
        total = self.price - ip
        

        taxt_total = (total * int(self.tax.name))/100
        with_tax = total+taxt_total
        newtot = round(with_tax,2)
        return newtot
class Attributes(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    att_typenew = models.IntegerField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)


class Coupon(models.Model):
    date_created = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100)
    co_code = models.CharField(max_length=25)
    co_count = models.IntegerField()
    co_discount = models.IntegerField()
    co_used = models.IntegerField()
    co_exp = models.DateField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)



class Order(models.Model):
    date_created = models.DateField(auto_now_add=True)
    dateandtime = models.DateTimeField(auto_now_add=True)
    order_id = models.CharField(max_length=150,default=str(uuid.uuid4())[:10])
    customer = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    current_status = models.BooleanField(default=False)
    product_list = models.ManyToManyField("OrderItems",related_name="orderitems")

    def __str__(self):
        return self.order_id

class OrderItems(models.Model):
    date_created = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="all_pro")
    qty = models.IntegerField(default=0)
    active_status = models.BooleanField(default=False)
    tracking_status = models.IntegerField(default=1)

    

    def __str__(self):
        return self.product.name
    
    def total_qty_wise(self):
        total = 0
        price = self.product.get_total()
        
        total = self.qty * price
        
        return total

   

        
   
class BillingAddress(models.Model):
    date_created = models.DateField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    post_code = models.CharField(max_length=100)
    customer = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)

class Wishlist(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="all_product")
    active_status = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

class BannerSettings(models.Model):
    image = models.ImageField()
    quote1 = models.CharField(max_length=100)
    quote2 = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    status = models.IntegerField()