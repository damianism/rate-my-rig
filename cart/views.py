from django.shortcuts import render, redirect, reverse
from django.contrib import messages 
from django.http import HttpResponseRedirect


def view_cart(request):
    """
    View to render contents of the cart
    """
    
    # no context needs to be passed in since it's stored in the session
    return render(request, "cart/cart.html")



def add_to_cart(request, pk):
    """ 
    Add a quantity of the specified product to the cart
    """

    # get quantity out of the form
    quantity = int( request.POST.get("quantity") )
    
    # get cart out of session if exists
    cart = request.session.get("cart", {} )

    if pk in cart:
        val = int(cart[pk]) + quantity
        if val > 5: # only 5 orders of a specific build can be placed!
            quantity = 5
            cart[pk] = 5
        else:
            cart[pk] = val
    else:
        cart[pk] = cart.get(pk, quantity)

    request.session["cart"] = cart
    
    messages.success(request, "Item(s) added to cart.")
    
    # redirect back to original page 
    #   - if item added from post_detail template, redirect back to post_detail template
    #   - if item added from home template, redirect back to home template
    previous_loc = request.META.get('HTTP_REFERER')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    

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
    

    
