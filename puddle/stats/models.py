from django.db import models

# Create your models here.
#MODEL FOR TOTAL SALE VALUE AND TOTAL NO. OF PRODUCTS ON SALE
class TotalSale(models.Model):
    #created_at, total_products_on_sale, total_val_of_onsale_prd

    total_products_on_sale = models.FloatField()
    total_val_of_onsale_prd = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.created_at