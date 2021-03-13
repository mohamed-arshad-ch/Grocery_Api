from django.shortcuts import render
from django.views import View
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from django.contrib.auth import login
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from .modelcontroller import *
from .models import *
import django_filters
from .serializers import *
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

# Register API


class RegisterUser(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
            "status":"success",
            "id":user.id
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        
        if serializer.is_valid():

            user = serializer.validated_data['user']
            login(request, user)
            main_data = super(LoginAPI, self).post(request, format=None)
            main_data.data['status'] = "success"
            newu = CustomUser.objects.get(username=request.data['username'])
            main_data.data['id'] = newu.id
            return main_data
        else:
            return Response(
                {
                    "data":serializer.errors,
                    "status":"error"
                }
            )


class CreateProduct(generics.GenericAPIView):
    serializer_class = ProductSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()
        return Response({
            "data": ProductSerializer(product, context=self.get_serializer_context()).data,
            "status": "success"
        })


class CreateCategory(generics.GenericAPIView):
    serializer_class = CategorySerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = serializer.save()
        return Response({
            "data": CategorySerializer(category, context=self.get_serializer_context()).data,
            "status": "success"
        })


class CreateOrder(generics.GenericAPIView):
    serializer_class = OrderSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        return Response({
            "data": ReadOrderSerializer(order, context=self.get_serializer_context()).data,
            "status": "success"
        })


class CreateOrderItem(generics.GenericAPIView):
    serializer_class = OrderItemSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        return Response({
            "data": OrderItemSerializer(order, context=self.get_serializer_context()).data,
            "status": "success"
        })


class CreateSubCategory(generics.GenericAPIView):
    serializer_class = SubCategorySerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        return Response({
            "data": SubCategorySerializer(order, context=self.get_serializer_context()).data,
            "status": "success"
        })


class CreateBillingAddress(generics.GenericAPIView):
    serializer_class = BillingAddressSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        billingaddress = serializer.save()
        return Response({
            "data": BillingAddressSerializer(billingaddress, context=self.get_serializer_context()).data,
            "status": "success"
        })


class CreateWishlist(generics.GenericAPIView):
    serializer_class = WishlistSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        wishlist = serializer.save()
        return Response({
            "data": WishlistSerializer(wishlist, context=self.get_serializer_context()).data,
            "status": "success"
        })


class CreateBanner(generics.GenericAPIView):
    serializer_class = BannerSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        banner = serializer.save()
        return Response({
            "data": BannerSerializer(banner, context=self.get_serializer_context()).data,
            "status": "success"
        })


class CreateCoupon(generics.GenericAPIView):
    serializer_class = CouponSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        coupon = serializer.save()
        return Response({
            "data": CouponSerializer(coupon, context=self.get_serializer_context()).data,
            "status": "success"
        })


class CreateAttributes(generics.GenericAPIView):
    serializer_class = AttributesSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        attributes = serializer.save()
        return Response({
            "data": AttributesSerializer(attributes, context=self.get_serializer_context()).data,
            "status": "success"
        })


class UpdateForProduct(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            queryset, status = ModelController(
                table=Product).get_one_content(val=kwargs['pk'])
            if status:

                serializer = ProductSerializer(queryset)

                return Response({"data": serializer.data, "status": "success"})
            else:
                return Response({"data": "Data Not Available", "status": "error"})
        except Product.DoesNotExist:
            return Response({"status": "error"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = ProductSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.save()
            return Response({"data": serializer.data, "status": "success"})
        else:
            errorr = serializer.errors
            errorr['status'] = "Error"

            return Response(errorr)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object().delete()
        return Response({"message": "deleted Successfully", "status": "success"})


class UpdateForCategory(generics.UpdateAPIView):
    serializer_class = CategorySerializer
    queryset = ChartOfAccounts.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            queryset, status = ModelController(
                table=ChartOfAccounts).get_one_content(val=kwargs['pk'])
            if status:
                serializer = CategorySerializer(queryset)

                return Response({"data": serializer.data, "status": "success"})
            else:
                return Response({"data": "Data Not Available", "status": "error"})

        except ChartOfAccounts.DoesNotExist:
            return Response({"status": "error"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = ProductSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.save()
            return Response({"data": serializer.data, "status": "success"})
        else:
            errorr = serializer.errors
            errorr['status'] = "Error"

            return Response(errorr)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object().delete()
        return Response({"message": "deleted Successfully", "status": "success"})


class UpdateForSubCategory(generics.UpdateAPIView):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            queryset, status = ModelController(
                table=SubCategory).get_one_content(val=kwargs['pk'])
            if status:
                serializer = SubCategorySerializer(queryset)

                return Response({"data": serializer.data, "status": "success"})
            else:
                return Response({"data": "Data Not Available", "status": "error"})

        except SubCategory.DoesNotExist:
            return Response({"status": "error"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = SubCategorySerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.save()
            return Response({"data": serializer.data, "status": "success"})
        else:
            errorr = serializer.errors
            errorr['status'] = "Error"

            return Response(errorr)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object().delete()
        return Response({"message": "deleted Successfully", "status": "success"})


class UpdateForOrderItem(generics.UpdateAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItems.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            queryset, status = ModelController(
                table=OrderItems).get_one_content(val=kwargs['pk'])
            if status:
                serializer = OrderItemSerializer(queryset)

                return Response({"data": serializer.data, "status": "success"})
            else:
                return Response({"data": "Data Not Available", "status": "error"})

        except SubCategory.DoesNotExist:
            return Response({"status": "error"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = OrderItemSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.save()
            return Response({"data": serializer.data, "status": "success"})
        else:
            errorr = serializer.errors
            errorr['status'] = "Error"

            return Response(errorr)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object().delete()
        return Response({"message": "deleted Successfully", "status": "success"})


class UpdateForCoupon(generics.UpdateAPIView):
    serializer_class = CouponSerializer
    queryset = Coupon.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            queryset, status = ModelController(
                table=Coupon).get_one_content(val=kwargs['pk'])
            if status:
                serializer = CouponSerializer(queryset)

                return Response({"data": serializer.data, "status": "success"})
            else:
                return Response({"data": "Data Not Available", "status": "error"})

        except Coupon.DoesNotExist:
            return Response({"status": "error"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = CouponSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.save()
            return Response({"data": serializer.data, "status": "success"})
        else:
            errorr = serializer.errors
            errorr['status'] = "Error"

            return Response(errorr)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object().delete()
        return Response({"message": "deleted Successfully", "status": "success"})


class UpdateForWishlist(generics.UpdateAPIView):
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            queryset, status = ModelController(
                table=Wishlist).get_one_content(val=kwargs['pk'])
            if status:
                serializer = WishlistSerializer(queryset)

                return Response({"data": serializer.data, "status": "success"})
            else:
                return Response({"data": "Data Not Available", "status": "error"})

        except Wishlist.DoesNotExist:
            return Response({"status": "error"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = WishlistSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.save()
            return Response({"data": serializer.data, "status": "success"})
        else:
            errorr = serializer.errors
            errorr['status'] = "Error"

            return Response(errorr)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object().delete()
        return Response({"message": "deleted Successfully", "status": "success"})


class UpdateForAttributes(generics.UpdateAPIView):
    serializer_class = AttributesSerializer
    queryset = Attributes.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            queryset, status = ModelController(
                table=Attributes).get_one_content(val=kwargs['pk'])
            if status:
                serializer = AttributesSerializer(queryset)

                return Response({"data": serializer.data, "status": "success"})
            else:
                return Response({"data": "Data Not Available", "status": "error"})

        except Attributes.DoesNotExist:
            return Response({"status": "error"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = AttributesSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.save()
            return Response({"data": serializer.data, "status": "success"})
        else:
            errorr = serializer.errors
            errorr['status'] = "Error"

            return Response(errorr)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object().delete()
        return Response({"message": "deleted Successfully", "status": "success"})


class UpdateForBanner(generics.UpdateAPIView):
    serializer_class = BannerSerializer
    queryset = BannerSettings.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            queryset, status = ModelController(
                table=BannerSettings).get_one_content(val=kwargs['pk'])
            if status:
                serializer = BannerSerializer(queryset)

                return Response({"data": serializer.data, "status": "success"})
            else:
                return Response({"data": "Data Not Available", "status": "error"})

        except BannerSettings.DoesNotExist:
            return Response({"status": "error"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = BannerSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.save()
            return Response({"data": serializer.data, "status": "success"})
        else:
            errorr = serializer.errors
            errorr['status'] = "Error"

            return Response(errorr)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object().delete()
        return Response({"message": "deleted Successfully", "status": "success"})


class UpdateForBillingAddress(generics.UpdateAPIView):
    serializer_class = BillingAddressSerializer
    queryset = BillingAddress.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            queryset, status = ModelController(
                table=BillingAddress).get_one_content(val=kwargs['pk'])
            if status:
                serializer = BillingAddressSerializer(queryset)

                return Response({"data": serializer.data, "status": "success"})
            else:
                return Response({"data": "Data Not Available", "status": "error"})

        except BillingAddress.DoesNotExist:
            return Response({"status": "error"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = BillingAddressSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.save()
            return Response({"data": serializer.data, "status": "success"})
        else:
            errorr = serializer.errors
            errorr['status'] = "Error"

            return Response(errorr)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object().delete()
        return Response({"message": "deleted Successfully", "status": "success"})


class UpdateForOrder(generics.UpdateAPIView):
    serializer_class = ReadOrderSerializer
    queryset = Order.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            queryset, status = ModelController(
                table=Order).get_one_content(val=kwargs['pk'])
            if status:
                serializer = ReadOrderSerializer(queryset)

                return Response({"data": serializer.data, "status": "success"})
            else:
                return Response({"data": "Data Not Available", "status": "error"})

        except Order.DoesNotExist:
            return Response({"status": "error"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = OrderSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.save()
            return Response({"data": serializer.data, "status": "success"})
        else:
            errorr = serializer.errors
            errorr['status'] = "Error"

            return Response(errorr)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object().delete()
        return Response({"message": "deleted Successfully", "status": "success"})


class SortAccounts(generics.ListAPIView):
    queryset = ChartOfAccounts.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name']
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'

    ordering_fields = ['name']


class PartialSearchForAccounts(generics.ListAPIView):

    queryset = ChartOfAccounts.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'

    def get(self, request):

        name = request.GET.get('name')

        instance = ChartOfAccounts.objects.filter(name__icontains=name)

        if instance.exists():

            serializer = CategorySerializer(instance, many=True)
            return Response({"data": serializer.data, "status": "success"})
        else:
            return Response({"data": "error", "status": "error"})


class SortProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name']
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'

    ordering_fields = ['name']


class PartialSearchForProduct(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'

    def get(self, request):

        name = request.GET.get('name')

        instance = Product.objects.filter(name__icontains=name)

        if instance.exists():

            serializer = ProductSerializer(instance, many=True)
            return Response({"data": serializer.data, "status": "success"})
        else:
            return Response({"data": "error", "status": "error"})


class SortSubCategory(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = "__all__"
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'

    ordering_fields = "__all__"


class PartialSearchForSubCategory(generics.ListAPIView):

    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'

    def get(self, request):

        name = request.GET.get('name')

        instance = SubCategory.objects.filter(name__icontains=name)

        if instance.exists():

            serializer = SubCategorySerializer(instance, many=True)
            return Response({"data": serializer.data, "status": "success"})
        else:
            return Response({"data": "error", "status": "error"})


class SortOrder(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = "__all__"
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'

    ordering_fields = "__all__"


class PartialSearchForOrder(generics.ListAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'

    def get(self, request):

        order_id = request.GET.get('order_id')

        instance = Order.objects.filter(order_id__icontains=order_id)

        if instance.exists():

            serializer = OrderSerializer(instance, many=True)
            return Response({"data": serializer.data, "status": "success"})
        else:
            return Response({"data": "error", "status": "error"})


class SortOrderItems(generics.ListAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = "__all__"
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'

    ordering_fields = "__all__"


class PartialSearchForOrderItems(generics.ListAPIView):

    queryset = OrderItems.objects.all()
    serializer_class = OrderItemSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'

    def get(self, request):

        tracking_status = request.GET.get('tracking_status')

        instance = OrderItems.objects.filter(
            tracking_status__icontains=tracking_status)

        if instance.exists():

            serializer = OrderItemSerializer(instance, many=True)
            return Response({"data": serializer.data, "status": "success"})
        else:
            return Response({"data": "error", "status": "error"})


class SortCoupon(generics.ListAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = "__all__"
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'

    ordering_fields = "__all__"


class PartialSearchForCoupon(generics.ListAPIView):

    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'

    def get(self, request):

        tracking_status = request.GET.get('tracking_status')

        instance = Coupon.objects.filter(
            tracking_status__icontains=tracking_status)

        if instance.exists():

            serializer = CouponSerializer(instance, many=True)
            return Response({"data": serializer.data, "status": "success"})
        else:
            return Response({"data": "error", "status": "error"})


class SortWishlist(generics.ListAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = "__all__"
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'

    ordering_fields = "__all__"


class PartialSearchForWishlist(generics.ListAPIView):

    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'

    def get(self, request):

        tracking_status = request.GET.get('tracking_status')

        instance = Wishlist.objects.filter(
            tracking_status__icontains=tracking_status)

        if instance.exists():

            serializer = WishlistSerializer(instance, many=True)
            return Response({"data": serializer.data, "status": "success"})
        else:
            return Response({"data": "error", "status": "error"})


class SortAttributes(generics.ListAPIView):
    queryset = Attributes.objects.all()
    serializer_class = AttributesSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = "__all__"
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'

    ordering_fields = "__all__"


class PartialSearchForAttributes(generics.ListAPIView):

    queryset = Attributes.objects.all()
    serializer_class = AttributesSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'

    def get(self, request):

        tracking_status = request.GET.get('tracking_status')

        instance = Attributes.objects.filter(
            tracking_status__icontains=tracking_status)

        if instance.exists():

            serializer = AttributesSerializer(instance, many=True)
            return Response({"data": serializer.data, "status": "success"})
        else:
            return Response({"data": "error", "status": "error"})


class SortBanner(generics.ListAPIView):
    queryset = BannerSettings.objects.all()
    serializer_class = BannerSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['id', 'quote1', 'quote2', 'active', 'status']
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'

    ordering_fields = "__all__"


class PartialSearchForBanner(generics.ListAPIView):

    queryset = BannerSettings.objects.all()
    serializer_class = BannerSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'

    def get(self, request):

        tracking_status = request.GET.get('tracking_status')

        instance = BannerSettings.objects.filter(
            tracking_status__icontains=tracking_status)

        if instance.exists():

            serializer = BannerSerializer(instance, many=True)
            return Response({"data": serializer.data, "status": "success"})
        else:
            return Response({"data": "error", "status": "error"})
