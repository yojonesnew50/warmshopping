import datetime
import os
from django.conf import settings
from django.shortcuts import render_to_response, RequestContext, Http404, HttpResponseRedirect, HttpResponse


from cart.models import Cart
from products.models import Featured, Product, Category



def home(request):
    featured_list = Featured.objects.filter(date_start__lte=datetime.datetime.now()).filter(date_end__gte=datetime.datetime.now())
    #import ipdb
    #ipdb.set_trace()
    #featured_products = featured_list[0].products.all()
    # these featured_products could be added to home page

    # If searching products, use .filter() not .all()
    products = Product.objects.all().order_by('-timestamp')[:10]
    categories= Category.objects.all().order_by('-timestamp')[:6]
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
    except:
        cart = False
        cartitems = None
        #firef
    if cart:
        cartitems = []
        for item in cart.cartitem_set.all():
            cartitems.append(item.product)

    return render_to_response("home.html", locals(), context_instance=RequestContext(request))

def my_custom_404_view(request):
    return render_to_response('404.html', {})