from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie,get_token
from django.http import JsonResponse
from django.contrib.auth import authenticate,login as django_login,logout as django_logout
from .models import Products
from .models import Wishlist
# Create your views here.
def home(request):
    return JsonResponse({"message": "HireFlow API is running"})


@ensure_csrf_cookie
def csrf(request):
    token=get_token(request)
    return JsonResponse({"csrfToken": token})

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    username=request.data['first_name']
    useremail=request.data['email']
    password=request.data['password']
    if (User.objects.filter(email=useremail).exists() or User.objects.filter(username=username).exists()):
         return Response({"message": "user already exists"}, status=400)
    else:
        user = User.objects.create_user(username, useremail, password)

    return Response({"message": "User created successfully"}, status=201)
@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    username=request.data['username']
    password=request.data['password']
    if not username or not password:
        return Response({"message":"username and password required"},status=400)
    user = authenticate(username=username, password=password)
    if user is not None:
        django_login(request,user)
        return Response({"message": "Login successful"},status =200) 
    else:
        # No backend authenticated the credentials
        return Response({"message": "Invalid infos"}, status=401)
@api_view(['POST'])
@permission_classes([AllowAny])
def add_products(request):
    username=request.data['username']
    password=request.data['password']
    user= authenticate(username=username,password=password)
    if user is not None:
        name=request.data['name']
        description=request.data['description']
        image= request.FILES.get('image')
        price=request.data['price']
        category=request.data['category']
        stock=request.data['stock']
        product =Products(name=name,description=description,image=image,price= price,category=category,stock=stock)
        product.save()
    else:
        return Response({'message': 'Please Login'})
    return Response(
    {"message": "Product created successfully"},status=201)
@api_view(['GET'])
@permission_classes([AllowAny])
def show_products(request):
    products=Products.objects.all().values()
    return JsonResponse(list(products),safe=False)
@api_view(['GET'])
@permission_classes([AllowAny])
def search(request):
    products_name=request.query_params.get('search_name', '')
    products=[]
    if products_name:
            search_names=Products.objects.filter(name__icontains=products_name)
        
    else:
        search_names=Products.objects.all()
    for product in search_names:
                    products.append(
                        {
                        'id': product.id,
                        'name': product.name,
                        'price': product.price,
                        'image': product.image.url if product.image else None,
                        'description':product.description
                    }
                    )
    return Response(products)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def wishlist(request):
     product_id=request.data['product_id']
     product= Products.objects.get(id=product_id)
     user=request.user
     wishlist, created = Wishlist.objects.get_or_create(user=user)
     wishlist.products.add(product)
     return Response({'message': 'Product added to wishlist'})
          
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def send_wishlist(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    products = []
    for product in wishlist.products.all():
          products.append({
           "id": product.id,
           "image": product.image.url if product.image else None,
           "name": product.name,
           "price": product.price,
           "description": product.description
          })
    return Response(products)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_product(request):
    product_id = request.data.get('product_id')

    wishlist, created = Wishlist.objects.get_or_create(
        user=request.user
    )

    try:
        product = Products.objects.get(id=product_id)
        wishlist.products.remove(product)

        return Response({
            'message': 'Product removed from wishlist'
        })

    except Products.DoesNotExist:
        return Response({
            'message': 'Product not found'
        }, status=404)
@api_view(['GET'])
@permission_classes([AllowAny])
def categories_clothes(request):
    category = request.query_params.get('category')

    products = Products.objects.filter(
        category=category
    ).values()

    return Response(list(products))
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_acount(request):
     user=request.user
     user.delete()
     return Response({"message": "Account deleted successfully"})
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    django_logout(request)
    return Response('logout succesfully')









          




