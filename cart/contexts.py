from django.shortcuts import get_object_or_404
from blog.models import Post


def cart_contents(request):
    """ 
    Ensures that the cart is available globally anywhere within the website
    """
    jdebug = 0
    if jdebug > 0: print( "cart_contents() " )

    
    # NOTE:
    # posts are reffered to as "build" since they hold configuration data
    
    # get cart out of session, return "" is it doesnt exist in request
    cart = request.session.get("cart", {})
    
    cart_items = []
    total = 0
    build_count = 0
    # base_price = 100.0  # charge for each configuration to be built
    for pk, quantity in cart.items():
        build = get_object_or_404(Post, pk=pk)
        total += quantity * build.price  # base_price
        build_count += quantity
        build_context = {"pk":pk, "quantity": quantity, "build": build}
        cart_items.append(build_context)
        
    context = {
        "cart_items": cart_items,
        "total": total,
        "build_count": build_count
    }
    
    if jdebug > 0:  print("cart_contents() context =", context)
    
    return context