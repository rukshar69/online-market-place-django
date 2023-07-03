from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import TotalSale
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class SalesChartView(TemplateView):
    template_name = 'stats/index.html'

    def get_context_data(self, **kwargs):
        stats = TotalSale.objects.all()
        for obj in stats:
                obj.created_at = obj.created_at.date()  # Convert DateTimeField to date
        context = super().get_context_data(**kwargs)
        context["qs"] = stats
        return context
    

# @login_required
# def index(request):
#         return render(request, 'stats/index.html')