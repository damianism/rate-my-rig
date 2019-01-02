from django.db import models
from blog.models import Post



class Order(models.Model):
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=40)
    postcode = models.CharField(max_length=10, blank=True)
    town_or_city = models.CharField(max_length=40)
    street_address1 = models.CharField(max_length=45)
    street_address2 = models.CharField(max_length=45, blank=True)
    county = models.CharField(max_length=40)
    date = models.DateField()
    
    def __str__(self):
        return "{}-{}-{}".format(self.id, self.date, self.full_name)
        
        
        
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order,  on_delete=models.CASCADE)
    build = models.ForeignKey(Post,  on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return "{} {} @ {}".format(self.quantity, self.build.title, self.build.price)