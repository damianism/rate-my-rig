from django.shortcuts import get_object_or_404
from posts.models import Post

def cart_contents(request):
    """ 
    Ensures that the cart is available globally anywhere within the website
    """
    
    # get cart out of session, return "" is it doesnt exist in request
    cart = request.session.get("cart", "")
    
    cart_items = []
    total = 0
    post_count = 0
    base_price = 100.0
    for pk, quantity in cart.items():
        post = get_object_or_404(Post, pk=item.id)
        