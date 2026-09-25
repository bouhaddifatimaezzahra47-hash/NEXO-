from django.urls import path
from . import views
urlpatterns = [
    path("", views.home),
    path("signup/", views.signup),
    path("login/", views.user_login),
    path("add_products/", views.add_products),
    path("show_products/", views.show_products),
    path("search/", views.search),
    path("wishlist/", views.wishlist),
    path("send_wishlist/", views.send_wishlist),
    path("delete_product/", views.delete_product),
    path("delete_acount/", views.delete_acount),
    path("logout/", views.logout),
    path("categories_clothes/", views.categories_clothes),

    path("csrf/",views.csrf)
]
