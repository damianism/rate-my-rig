from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.http import HttpResponseRedirect

@login_required
def view_cart(request):
    """
    View to render contents of the cart
    """
    
    # no context needs to be passed since it's stored in the session
    return render(request, "cart/cart.html")


@login_required
def add_to_cart(request, pk):
    """ 
    Add a quantity of the specified product to the cart
    """
    # pk = str(pk)
    # get quantity out of the form
    try:
        quantity = int( request.POST.get("quantity") )
    except TypeError:
        # preventing TypeError on cloud9 and Server Error (500) on heroku
        messages.info(request, "You may now add to cart.")
        return redirect( 'blog-home' )
        
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
    print("previous_loc = ", previous_loc)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    # NOTE! ASK ABOUT THIS! REMOVE IF US OF "HttpResponseRedirect" IS OK!
    # if "post" in previous_loc:
    #     return redirect( 'post-detail', pk=pk )
    # else:
    #     return redirect( 'blog-home' )
    
    
@login_required  
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
    

    
