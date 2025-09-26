# website/api/views.py

import json
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from website.models import Products
from website.api.serialization.product_serializer import ProductSerializer

User = get_user_model()


# ---------------- API: Login and Token ----------------
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login_api(request):
    """
    Login API: Authenticates user and generates token
    """
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return Response({"success": False, "error": "Invalid JSON"}, status=400)

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return Response({"success": False, "error": "Username and password required"}, status=400)

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"success": False, "error": "Invalid credentials"}, status=401)

    # create or get token
    token, created = Token.objects.get_or_create(user=user)

    return Response({
        "success": True,
        "username": user.username,
        "is_staff": user.is_staff,
        "token": token.key
    })


# ---------------- API: Signup ----------------
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    """
    Signup API: Create new user
    """
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return Response({"success": False, "error": "Invalid JSON"}, status=400)

    username = data.get("username")
    password = data.get("password")
    email = data.get("email", "")

    if not username or not password:
        return Response({"success": False, "error": "Username and password required"}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({"success": False, "error": "Username already exists"}, status=400)

    user = User.objects.create_user(username=username, password=password, email=email)
    return Response({"success": True, "username": user.username})


# ---------------- API: Product List ----------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_list(request):
    """
    Returns all products. Requires token authentication.
    """
    serialized = ProductSerializer(Products.objects.all(), many=True)
    return Response(serialized.data)
