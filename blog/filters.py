import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    
    
    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
        
        )
    
    ordering = django_filters.ChoiceFilter(label='Order by', choices=CHOICES, method='filter_by_order')
    
    class Meta:
        model = Post
        fields = [
            'cpu', 
            'gpu', 
            'ram',
            'psu'
        ]
        
    def filter_by_order(self, queryset, name, value):
        expression = 'date_posted' if value == 'ascending' else '-date_posted'
        return queryset.order_by(expression)
        