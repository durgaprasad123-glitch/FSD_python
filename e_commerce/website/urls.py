from django.urls import path, include
from . import views

urlpatterns = [
    # Root opens dashboard directly
    path('', views.home, name='home'),

    # Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Products & Cart
    path('products/', views.product_list_view, name='product_list'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/<int:product_id>/', views.update_cart, name='update_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    # Logout
    path('logout/', views.logout_view, name='logout'),


    # Search
    path('search/', views.search, name='search'),

    # API URLs (React frontend)
    path('api/', include('website.api.urls')),
]
