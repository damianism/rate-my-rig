from django.urls import path
from .views import do_search, pre_search


urlpatterns = [
    path('pre', pre_search, name="pre-search"),
    path('', do_search, name="search"),
]