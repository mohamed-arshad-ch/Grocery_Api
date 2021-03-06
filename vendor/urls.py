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
    path('mainadmin/subcategory',CreateSubCategory.as_view()),
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

    path('mainadmin/categoryall/all',SortAccounts.as_view()),
    path('mainadmin/productall/all',SortProducts.as_view()),
    path('mainadmin/subcategoryall/all',SortSubCategory.as_view()),
    path('user/orderall/all',SortOrder.as_view()),
    path('user/orderitemsall/all',SortOrderItems.as_view()),
    path('mainadmin/couponall/all',SortCoupon.as_view()),
    path('user/wishlistall/all',SortWishlist.as_view()),
    path('mainadmin/attributesall/all',SortAttributes.as_view()),
    path('mainadmin/bannerall/all',SortBanner.as_view()),
    path('user/billingaddressall/all',SortAccounts.as_view()),


    path('mainadmin/categoryall/search',PartialSearchForAccounts.as_view()),
    path('mainadmin/productall/search',PartialSearchForProduct.as_view()),
    path('mainadmin/subcategoryall/search',PartialSearchForSubCategory.as_view()),
    path('user/orderall/search',PartialSearchForOrder.as_view()),
    path('user/orderitemsall/search',PartialSearchForOrderItems.as_view()),
    path('mainadmin/couponall/search',PartialSearchForCoupon.as_view()),
    path('user/wishlistall/search',PartialSearchForWishlist.as_view()),
    path('mainadmin/attributesall/search',PartialSearchForAttributes.as_view()),
    path('mainadmin/bannerall/search',PartialSearchForBanner.as_view()),
    path('user/billingaddressall/search',SortAccounts.as_view()),
    
   
]


