from django.urls import path,include,re_path
from .views import *
from knox import views as knox_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    
    path('user/register',RegisterUser.as_view()),
    path('user/login',LoginAPI.as_view()),
    path('mainadmin/product',CreateProduct.as_view()),
    # path('mainadmin/add-subcategory',CreateProduct.as_view()),
    path('mainadmin/category',CreateCategory.as_view()),
    path('user/order',CreateOrder.as_view()),
    path('user/orderitems',CreateOrderItem.as_view()),
    path('mainadmin/subcategory',CreateCategory.as_view()),
    path('user/billingaddress',CreateBillingAddress.as_view()),
    path('mainadmin/banner',CreateBanner.as_view()),
    path('user/wishlist',CreateWishlist.as_view()),
    path('mainadmin/coupon',CreateCoupon.as_view()),
    path('mainadmin/attributes',CreateAttributes.as_view()),
    
    path('mainadmin/product/<str:pk>',UpdateForProduct.as_view()),
    path('mainadmin/subcategory/<str:pk>',UpdateForSubCategory.as_view()),
    path('user/order/<str:pk>',UpdateForOrder.as_view()),
    path('mainadmin/category/<str:pk>',UpdateForCategory.as_view()),
    path('user/orderitems/<str:pk>',UpdateForOrderItem.as_view()),
    path('mainadmin/coupon/<str:pk>',UpdateForCoupon.as_view()),
    path('user/wishlist/<str:pk>',UpdateForWishlist.as_view()),
    path('mainadmin/attributes/<str:pk>',UpdateForAttributes.as_view()),
    path('mainadmin/banner/<str:pk>',UpdateForBanner.as_view()),
    path('user/billingaddress/<str:pk>',UpdateForBillingAddress.as_view()),


   
]


