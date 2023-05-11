from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user =  models.ForeignKey(User, default=1, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name