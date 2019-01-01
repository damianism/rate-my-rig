from django.shortcuts import render, redirect, reverse



def view_cart(request):
    """
    View to render contents of the cart
    """
    
    # no context needs to be passed since it's stored in the session
    return render(request, "cart/cart.html")
    
    
def add_to_cart(request, pk):
    """ 
    Add a quantity of the specified product to the cart
    """
    
    # get quantity out of the form
    quantity = int( request.POST.get("quantity") )
    
    # get cart out of session if exists
    cart = request.session.get("cart", {} )
    cart[pk] = cart.get( pk, quantity )
    
    request.session["cart"] = cart
    print("cart 'add_to_cart' = ", cart)
    
    # return redirect( reverse('blog-home') )
    return redirect( 'blog-home' )
    
    
    
def adjust_cart(request, pk):
    """
    view to adjust the quantity of the specified post to the specified ammount 
    """
    
    quantity = int( request.POST.get("quantity") )
    
    cart = request.session.get("cart", {})
    
    if quantity > 0:
        cart[pk] = quantity
    else:
        cart.pop(pk)
    
    request.session["cart"] = cart
    
    return redirect( reverse('view-cart') )