from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import OrderForm, MakePaymentForm
from .models import OrderLineItem
from django.utils import timezone
from django.contrib import messages 
from blog.models import Post
import stripe


stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
        
            cart = request.session.get("cart", {})
            total = 0
            for pk, quantity in cart.items():
                build = get_object_or_404(Post, pk=pk)
                total += quantity * build.price
                order_line_item = OrderLineItem(
                    order = order,
                    build = build,
                    quantity = quantity
                )
                order_line_item.save()
                
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "GBP",
                    description = request.user.email,
                    card = payment_form.cleaned_data["stripe_id"],
                    )
            except stripe.error.CardError:
                messages.error(request, "your card was declined!")
                
            if customer.paid:
                messages.success(request, "You have successfully paid!")
                request.session["cart"] = {}
                # return redirect( reverse("blog-home") )
                return redirect( "blog-home")
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We are unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    
    context = {
        "order_form": order_form,
        "payment_form": payment_form,
        "publishable": settings.STRIPE_PUBLISHABLE
    }
        
    return render(request, "checkout/checkout.html", context)