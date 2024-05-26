from django.db import models

# Create your models here.

class ProductModel(models.Model):
    # Image = models.ImageField(upload_to='image/')
    Prod_Name =models.CharField(max_length=254)
    Prod_price =models.IntegerField()
    Prod_offer =models.CharField(max_length=254)
    Prod_decription =models.TextField()
    Prod_use=models.CharField(max_length=254)

    def __str__(self):
        return self.Prod_Name