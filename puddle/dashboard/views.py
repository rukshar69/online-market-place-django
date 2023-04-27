from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from item.models import Item

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'items': items,
    })


@login_required
def approvals(request):
    items = Item.objects.filter(is_allowed=False)

    return render(request, 'dashboard/approval_list.html', {
        'items': items,
    })