from item.models import Item
from .models import TotalSale
from django.db.models import Sum

def calculate_stats():
    items = Item.objects.filter(is_sold=False , is_allowed=True)
    total_products_on_sale = items.count()
    sum_result = items.aggregate(total_sum=Sum('price'))
    total_val_of_onsale_prd = sum_result['total_sum']
    # Create a new instance of the model object with values
    my_object = TotalSale()
    my_object.total_products_on_sale = total_products_on_sale
    my_object.total_val_of_onsale_prd = total_val_of_onsale_prd
    # Save the object to the database
    my_object.save()