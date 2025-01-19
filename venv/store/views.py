from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product, CustomUser, Cart, ContactMessage
from .forms import ProductForm, ProductUpdateForm, CustomUserCreationForm, LoginForm,FilterProduits,ContactForm

def home(request):
    return render(request, 'pages/acceuil.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = ContactMessage(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            contact_message.save()
            return redirect('home')
    else:
        form = ContactForm()
    
    return render(request, 'pages/contact.html', {'form': form})

def about(request):
    return render(request, 'pages/about.html')

def list_products(request):
    products = Product.objects.all()
    return render(request, 'pages/products.html', {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'pages/product_detail.html', {'product': product})

def filterproduit(request):
    if request.method == 'POST':
        form = FilterProduits(request.POST)
        products = Product.objects.all()
        if form.is_valid():
            cleaned_data = form.cleaned_data
            if cleaned_data.get('name'):
                products = products.filter(nameicontains=cleaned_data['name'])
            if cleaned_data.get('price'):
                products = products.filter(pricelte=cleaned_data['price'])
            if cleaned_data.get('category'):
                products = products.filter(category=cleaned_data['category'])
            if cleaned_data.get('type'):
                products = products.filter(type=cleaned_data['type'])
    else:
        form = FilterProduits()
        products = Product.objects.all()

    print(f"Form data: {form.cleaned_data if form.is_valid() else 'Form is not valid'}")
    print(f"Filtered products: {products}")

    
    return render(request, 'pages/fproducts.html', {'form': form, 'products': products})


def signup_or_login(request):
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST, prefix='signup')
        login_form = LoginForm(request.POST, prefix='login')

        if 'signup-submit' in request.POST and signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            return redirect('home')

        elif 'login-submit' in request.POST and login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        signup_form = CustomUserCreationForm(prefix='signup')
        login_form = LoginForm(prefix='login')

    return render(request, 'pages/auth.html', {'signup_form': signup_form, 'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def add_to_cart(request, product_id, quantity=1):
    product = get_object_or_404(Product, pk=product_id)
    user = request.user
    cart_item, created = Cart.objects.get_or_create(user=user, product=product)
    if not created:
        if 'quantity' in request.POST:
            quantity = int(request.POST['quantity'])
        cart_item.quantity = int(quantity)
        cart_item.save()
    return redirect('my_cart')

@login_required
def get_cart(request):
    user = request.user
    cart_items = Cart.objects.filter(user=request.user).select_related('product')
    products_in_cart = [
        {"id": item.product.id, "name": item.product.name, "price": item.product.price,"image":item.product.image, "quantity": item.quantity, "type":item.product.type , 'total': item.product.price * item.quantity}
        for item in cart_items
    ]
    total = sum([i["price"] * i["quantity"] for i in products_in_cart])
    return render(request, 'pages/cart.html', {'products': products_in_cart, 'total': total})

@login_required
def delete_from_cart(request, product_id):
    cart_item = get_object_or_404(Cart, user_id=request.user.id, product_id=product_id)
    if cart_item.user != request.user:
        return redirect('my_cart')
    cart_item.delete()
    return redirect('my_cart')
