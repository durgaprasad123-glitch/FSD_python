# import json
# from django.http import JsonResponse
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
# from django.middleware.csrf import get_token
# from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# from django.shortcuts import redirect  
# from django.contrib.auth.models import User
# from .models import Products
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages

# # ---------------- Web Views ----------------
# def home(request):
#     products=Products.objects.all()
#     context={
#         'Products':products
#         }
#     return render(request, "website/index.html",context)

# def search(request):
#     return render(request, "search.html")

# # ---------------- Product APIs ----------------
# # def product_list(request):
# #     if request.method == "GET":
# #         products = list(Products.objects.values())
# #         return JsonResponse(products, safe=False)

# # def product_detail(request, product_name):
# #     if request.method == "GET":
# #         try:
# #             product = Products.objects.get(name=product_name)
# #             return JsonResponse({
# #                 "id": product.id,
# #                 "name": product.name,
# #                 "price": product.price,
# #                 "description": product.description,
# #                 "stock": product.stock
# #             })
# #         except Products.DoesNotExist:
# #             return JsonResponse({"error": "Product not found"}, status=404)

# # @csrf_exempt
# # def add_product(request):
# #     print("getting error here")
# #     if request.method == "POST":
# #         # if not request.user.is_authenticated:
# #         #     return JsonResponse({"success": False, "error": "Not authenticated"}, status=401)
# #         try:
# #             data = json.loads(request.body)
# #             product = Products.objects.create(
# #                 name=data.get("name"),
# #                 price=data.get("price"),
# #                 description=data.get("description", ""),
# #                 stock=data.get("stock", 0)
# #             )
# #             return JsonResponse({"success": True, "id": product.id})
# #         except Exception as e:
# #             return JsonResponse({"success": False, "error": str(e)})
# #     return JsonResponse({"success": False, "error": "POST required"}, status=400)

# # @csrf_exempt
# # def update_product(request, product_id):
# #     if request.method == "PUT":
# #         try:
# #             data = json.loads(request.body)
# #             product = Products.objects.get(id=product_id)
# #             product.name = data.get("name", product.name)
# #             product.price = data.get("price", product.price)
# #             product.description = data.get("description", product.description)
# #             product.stock = data.get("stock", product.stock)
# #             product.save()
# #             return JsonResponse({"success": True})
# #         except Products.DoesNotExist:
# #             return JsonResponse({"error": "Product not found"}, status=404)
# #         except Exception as e:
# #             return JsonResponse({"success": False, "error": str(e)})
# #     return JsonResponse({"success": False, "error": "PUT required"}, status=400)

# # @csrf_exempt
# # def delete_product(request, product_id):
# #     if request.method == "DELETE":
# #         try:
# #             product = Products.objects.get(id=product_id)
# #             product.delete()
# #             return JsonResponse({"success": True})
# #         except Products.DoesNotExist:
# #             return JsonResponse({"error": "Product not found"}, status=404)
# #     return JsonResponse({"success": False, "error": "DELETE required"}, status=400)

# # # ---------------- Auth APIs ----------------
# # @csrf_exempt
# # def login_api(request):
# #     if request.method == "POST":
# #         try:
# #             data = json.loads(request.body)
# #             user = authenticate(username=data.get("username"), password=data.get("password"))
# #             if user:
# #                 login(request, user)
# #                 return JsonResponse({
# #                     "success": True,
# #                     "username": user.username,
# #                     "is_staff": user.is_staff,  # Add this
# #                 })
# #             return JsonResponse({"success": False, "error": "Invalid credentials"}, status=401)
# #         except Exception as e:
# #             return JsonResponse({"success": False, "error": str(e)})
# #     return JsonResponse({"success": False, "error": "POST required"}, status=400)


# # @csrf_exempt
# # def signup(request):
# #     if request.method == "POST":
# #         try:
# #             data = json.loads(request.body)
# #             username = data.get("username")
# #             password = data.get("password")
# #             email = data.get("email", "")

# #             if not username or not password:
# #                 return JsonResponse({"success": False, "error": "Username and password required"}, status=400)

# #             if User.objects.filter(username=username).exists():
# #                 return JsonResponse({"success": False, "error": "Username already exists"}, status=400)

# #             user = User.objects.create_user(username=username, password=password, email=email)
# #             return JsonResponse({"success": True, "username": user.username})
# #         except Exception as e:
# #             return JsonResponse({"success": False, "error": str(e)})
# #     return JsonResponse({"success": False, "error": "POST required"}, status=400)

# # # ---------------- CSRF Token ----------------
# # @ensure_csrf_cookie
# # def get_csrf_token(request):
# #     return JsonResponse({"csrfToken": get_token(request)})

# # def check_auth(request):
# #     if request.user.is_authenticated:
# #         return JsonResponse({
# #             "authenticated": True,
# #             "username": request.user.username,
# #             "is_staff": request.user.is_staff,  # Add this line
# #         })
# #     return JsonResponse({"authenticated": False})


# # ---------------- Users & Dashboard ----------------
# # keep existing add-user functionality untouched
# def users_list(request):
#     users = list(User.objects.values("id", "username", "email"))
#     return JsonResponse(users, safe=False)

# def dashboard_stats(request):
#     total_products = Products.objects.count()
#     total_users = User.objects.count()
 
#     return JsonResponse({"total_products": total_products, "total_users": total_users})
# def login(request):
#     username=request.POST.get('username')
#     password=request.POST.get('password')
#     user=authenticate(request,username=username,password=password)
#     if user is not None:
#         auth_login(request,user)
#         return redirect('home')
#     return render(request, "website/login.html")
# def logout(request):
#     return render(request, "website/logout.html")

# # Product list HTML view
# def product_list_view(request):
#     products = Products.objects.all()
#     return render(request, 'website/product_list.html', {'products': products})
# # Cart helpers
# def get_cart(request):
#     return request.session.get('cart', {})

# def add_to_cart(request, product_id):
#     if request.method == "POST":
#         product = get_object_or_404(Products, id=product_id)
#         cart = request.session.get('cart', {})
#         if str(product_id) in cart:
#             cart[str(product_id)] += 1
#         else:
#             cart[str(product_id)] = 1
#         request.session['cart'] = cart
#         messages.success(request, f"Added {product.name} to cart!")
#     return redirect('product_list')



# # Cart view
# def cart_view(request):
#     cart = request.session.get('cart', {})
#     cart_items = []

#     total_price = 0
#     for product_id, qty in cart.items():
#         product = get_object_or_404(Products, id=product_id)
#         subtotal = product.price * qty
#         total_price += subtotal
#         cart_items.append({
#             'product': product,
#             'quantity': qty,
#             'subtotal': subtotal
#         })

#     context = {
#         'cart_items': cart_items,
#         'total_price': total_price
#     }
#     return render(request, 'website/cart.html', context)

# def update_cart(request, product_id):
#     if request.method == 'POST':
#         quantity = int(request.POST.get('quantity', 1))
#         cart = get_cart(request)
#         if quantity > 0:
#             cart[str(product_id)] = quantity
#         else:
#             cart.pop(str(product_id), None)
#         request.session['cart'] = cart
#     return redirect('cart')

# def remove_from_cart(request, product_id):
#     cart = get_cart(request)
#     cart.pop(str(product_id), None)
#     request.session['cart'] = cart
#     return redirect('cart')
# #product list view for rendering in template
# def checkout_view(request):
#     # Later you can add payment, shipping, etc.
#     return render(request, 'website/checkout.html')
# def login_view(request):
#     error = None
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             if user.is_superuser:
#                 return redirect("dashboard")
#             return redirect("home")
#         else:
#             error = "Invalid username or password"
#     return render(request, "website/login.html", {"error": error})
import json
from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.middleware.csrf import get_token
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model

from .models import Products

User = get_user_model()


# ---------------- Web Views ----------------
def home(request):
    # Redirect root URL directly to dashboard
    return redirect('dashboard')


def search(request):
    """Search page."""
    return render(request, "website/search.html")


# ---------------- Product Views ----------------
def product_list_view(request):
    products = Products.objects.all()
    return render(request, 'website/product_list.html', {'products': products})


# ---------------- Cart Helpers ----------------
def get_cart(request):
    return request.session.get('cart', {})


def add_to_cart(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Products, id=product_id)
        cart = get_cart(request)
        cart[str(product_id)] = cart.get(str(product_id), 0) + 1
        request.session['cart'] = cart
        messages.success(request, f"Added {product.name} to cart!")
    return redirect('product_list')


def cart_view(request):
    cart = get_cart(request)
    cart_items = []
    total_price = 0

    for product_id, qty in cart.items():
        product = get_object_or_404(Products, id=product_id)
        subtotal = product.price * qty
        total_price += subtotal
        cart_items.append({'product': product, 'quantity': qty, 'subtotal': subtotal})

    return render(request, 'website/cart.html', {'cart_items': cart_items, 'total_price': total_price})


def update_cart(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = get_cart(request)
        if quantity > 0:
            cart[str(product_id)] = quantity
        else:
            cart.pop(str(product_id), None)
        request.session['cart'] = cart
    return redirect('cart')


def remove_from_cart(request, product_id):
    cart = get_cart(request)
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('cart')


def checkout_view(request):
    return render(request, 'website/checkout.html')


# ---------------- Auth / Login / Logout ----------------
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard') if request.user.is_superuser else redirect('product_list')

    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)
            return redirect('dashboard') if user.is_superuser else redirect('product_list')
        else:
            error = "Invalid username or password"

    return render(request, "website/login.html", {"error": error})


def logout_view(request):
    # Logs out the user and redirects to login page
    auth_logout(request)
    return redirect('login') 

def dashboard_view(request):
    # Open dashboard directly without login
    products = Products.objects.all()
    users = User.objects.all()
    context = {
        "products": products,
        "users": users,
        "current_year": datetime.now().year
    }
    return render(request, "website/dashboard.html", context)



@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({"csrfToken": get_token(request)})


def check_auth(request):
    if request.user.is_authenticated:
        return JsonResponse({"authenticated": True, "username": request.user.username, "is_staff": request.user.is_staff})
    return JsonResponse({"authenticated": False})


# ---------------- Users & Dashboard Stats ----------------
def users_list(request):
    users = list(User.objects.values("id", "username", "email"))
    return JsonResponse(users, safe=False)


def dashboard_stats(request):
    return JsonResponse({
        "total_products": Products.objects.count(),
        "total_users": User.objects.count()
    })
