from django.db import models
from django.contrib.auth.models import User


# Create your models here.
CATEGORY = (
    ('Stationery', 'Stationery'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)
class Product(models.Model):
    name = models.CharField(max_length=100,  null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveBigIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return f'{self.name} : {self.quantity}'
    
class Order(models.Model):
    Product = models.ForeignKey(Product,on_delete=models.CASCADE, null=True)
    Staff = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    order_quantity = models.PositiveBigIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        if self.Staff:
            return f'{self.Product} ordered by {self.Staff.username}'
        else:
            return f"Order ID: {self.id} - {self.Product.name} : {self.order_quantity} (No staff assigned)"