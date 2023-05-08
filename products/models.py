from django.db import models

class Products(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', null=True)


    def __str__(self) -> str:
        return self.name