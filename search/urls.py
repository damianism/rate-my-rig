from django.urls import path
from .views import do_search, search_view


urlpatterns = [
    path('', search_view, name="search"),
    path('results/', do_search, name="search-results"),
]