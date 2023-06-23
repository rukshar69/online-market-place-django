import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
from datetime import date

def main():
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)

    response = supabase.table('item_item').select("*").execute()
    #print(len(response.data))

    count = 0
    total_price = 0
    for r in response.data:
        if r['is_sold'] == False and r['is_allowed'] == True:
            count += 1
            total_price += r['price']
    #print('total price: ', str(total_price))

    stats_response = supabase.table('stats_totalsale').select("*").execute()
    #print(len(stats_response.data))
    id = len(stats_response.data) + 1
    total_products_on_sale = count 
    total_val_of_onsale_prd = total_price
    created_at  = str(date.today())

    data, count = supabase \
    .table('stats_totalsale') \
    .insert({"id": id, "total_products_on_sale": total_products_on_sale,"total_val_of_onsale_prd":total_val_of_onsale_prd,
            "created_at":created_at }) \
    .execute()


if __name__ == '__main__':
    main()