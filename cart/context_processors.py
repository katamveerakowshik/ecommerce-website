from .models import Cart

def cart(request):
    try:
        cart = Cart.objects.get(id=request.session.get('cart_id'))
    except Cart.DoesNotExist:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
    
    return {'cart': cart} 