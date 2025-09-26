from django.urls import path
from website.api import views
from website import views as web_views

from rest_framework.authtoken import views as drf_views

urlpatterns = [
    path('token/', drf_views.obtain_auth_token, name='api_token_auth'),

    path('products/', views.product_list, name='product-list'),
    path("login/", views.login_api, name="login"),
    path("signup/", views.signup, name="signup"),

    path('api/products/', views.product_list, name='product-list'),
]
