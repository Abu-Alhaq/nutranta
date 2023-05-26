from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
STATE_CHOICES = (
    ('Kot Begum', 'Kot Begum'),
    ('Thokar Naiz baig','Thokar Naiz baig'),
    ('Shah Alam Market','Shah Alam Market'),
    ('Model Town','Model Town'),
    ('wapda Town','wapda Town'),
    ('Gulshan Ravi','Gulshan Ravi'),
    ('Gulberg','Gulberg'),
    ('Garden Town','Garden Town'),
    ('Faisal Town','Faisal Town'),
    ('DHA','DHA'),
    ('Cantt','Cantt'),
    ('Johar Town','Johar Town'),
    ('Bahria Town','Bahria Town'),
    ('Askari','Askari'),
    ('Valencia','Valencia'),
    ('Punjab Society','Punjab Society'),
    ('Punjab Coop Housing Society','Punjab Coop Housing Society'),
    ('Punjab Govt Servants Housing Foundation','Punjab Govt Servants Housing Foundation'),
    ('Punjab Small Industries Colony','Punjab Small Industries Colony'),
    ('Punjab University Employees Society','Punjab University Employees Society'),
    ('Punjab University Society','Punjab University Society'),
    ('Punjab Govt Employees Society','Punjab Govt Employees Society'),
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES = (
    ('v','vegetables'),
    ('f','fruits'),
    ('d','dairy'),
    ('fi','fish')
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    product_image = models.ImageField(upload_to='productimg')
    total_calroes = models.FloatField(default=0)
    total_fat = models.FloatField(default=0)
    total_protein = models.FloatField(default=0)
    total_carbohydrates = models.FloatField(default=0)
    total_sodium = models.FloatField(default=0)
    total_sugar = models.FloatField(default=0)
    total_cholesterol = models.FloatField(default=0)
    total_potassium = models.FloatField(default=0)
    total_calcium = models.FloatField(default=0)
    total_vitamin_d = models.FloatField(default=0)
    total_fiber = models.FloatField(default=0)

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_calroes = models.IntegerField(default=0)
    


    def __str__(self):
        return str(self.id)


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_calroes = models.IntegerField(default=0)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    address = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id + " " + self.address + " " + self.locality + " " + self.city + " " + self.state + " " + str(self.zipcode))
    


