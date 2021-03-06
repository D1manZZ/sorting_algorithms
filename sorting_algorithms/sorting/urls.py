from django.urls import path
from .views import *

urlpatterns = [
    path('', SortNums.as_view(), name='sort_nums'),
    path('sort_data/', SortData.as_view(), name='sort_data')
]