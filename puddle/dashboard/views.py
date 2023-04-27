from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from item.models import Item

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)
    items_not_approved = Item.objects.filter(created_by=request.user, is_allowed = False)
    items_approved = Item.objects.filter(created_by=request.user, is_allowed = True)

    return render(request, 'dashboard/index.html', {
        #'items': items,
        'items_not_approved': items_not_approved,
        'items_approved':items_approved,
    })


@login_required
def approvals(request):
    items = Item.objects.filter(is_allowed=False)

    return render(request, 'dashboard/approval_list.html', {
        'items': items,
    })