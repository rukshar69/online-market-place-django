from django.urls import path
from .views import SalesChartView
from . import views

app_name = 'stats'

urlpatterns = [
    path('', SalesChartView.as_view(), name='index'),
]