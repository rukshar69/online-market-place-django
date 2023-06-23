# online-market-place-django

A simple **online-merch-store**. 

Link to online app: https://online-market-place-django.vercel.app/ 

Backend: Django

Frontend: Tailwind based HTML/CSS

App Hosting: Vercel

Database: PostgreSQL (Hosted on [Supabase](https://app.supabase.com/projects) )

Image Hosting: Google Drive API using Python's [Django Google Drive Storage](https://django-googledrive-storage.readthedocs.io/en/latest/) package

# Features

- Signup, login, and logout
- The [Homepage](https://online-market-place-django.vercel.app/ ) lists the 6 newest unsold products added by users and then approved by the admin(superuser)
- The [Browse](https://online-market-place-django.vercel.app/items/) page allows for searching for an admin-approved unsold items/products using category and text-query. The text-query searches for the matching text in the Item's *name and description* fields. A button to clear the filters is also added.
- The [Dashboard](https://online-market-place-django.vercel.app/dashboard/) page shows the products added by the currently logged in user. It's divided in 2 parts. One showing items approved by the admin and the other showing items waiting to be approved by the admin.
- The [New Item](https://online-market-place-django.vercel.app/items/new/) page allows logged in users to add new products by entering its name, category, price, description, and image. For now, there're 4 categories: Toys, Clothes, Furnitures, and Jewelery.
- Clicking on any item/product card (seen on homepage, dashboard, and browse page) takes one to the item detail page that shows the details of the product/item. 
    - If the detail page's visitor is the owner of the item, they are also shown 2 buttons **Edit and Delete**. Edit button allows to change any info about the item and the Delete button removes the item's info. from the databse. 
        - In the edit page, there's a checkbox for *is_sold* field. If this box is checked and then saved, the item won't appear in the browse or homepage anymore since those pages only show unsold items.
        - If the item is sold, it appears in the *sold* section of the user's dashboard. In such a case, the user can't edit the product.
    - If the visitor is not the owner of that item, the button **Contact Seller** appears. Here one can send a message to the owner of that item. 
    - At the bottom of the detail page for an item, at most 3 item cards of the same category not owned by the logged in user will appear
- The [Inbox](https://online-market-place-django.vercel.app/inbox/) page lists the conversations for items where the sellers have been contacted. Clicking on a conversation leads one to the chatroom where one can send further messages to the seller.
- For superusers, there is an additional button in the nav bar named *Approval* that lists all the items that haven't been approved by the superuser(admin). The admin clicks on an item that leads them to a page to mark the check box for approving the item to appear in homepage and browse page.

# References
- [YouTube tutorial to construct this project locally](https://www.youtube.com/watch?v=ZxMB6Njs3ck)
- [Django Google Drive Storage](https://django-googledrive-storage.readthedocs.io/en/latest/)
- [Vercel tutorial](https://www.makeuseof.com/django-app-vercel-host-free/)
- [Supabase tutorial](https://youtu.be/YAI3omsUmpE)