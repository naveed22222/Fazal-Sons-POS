from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from django.http import Http404
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db import connections
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


def DictinctFetchAll(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]


# FUNCTION THAT CREATE TOKEN WHEN USER IS CREATED
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class MyLimitOffsetPagination(LimitOffsetPagination):
    limit_query_param = 'limit'
    offset_query_param = 'Starting'


# OUTLET
class AddOutletView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializer
    pagination_class = None


class OutletGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializer
    pagination_class = None


# BRAND
class AddBrandView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    pagination_class = MyLimitOffsetPagination


class BrandGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


@api_view(['GET'])
def SearchBrandView(request, code):
    brand_name = code
    brand = Brand.objects.filter(brand_name__icontains=brand_name)
    if len(brand) > 0:
        serializer = BrandSerializer(brand, many=True)
        param = {
            'status': 200,
            'results': serializer.data,
        }
        return Response(param)
    return Response("Not Found")


# ATTRIBUTES TYPE
class AddAttributeTypeView(generics.ListCreateAPIView):
    queryset = AttributeType.objects.all()
    serializer_class = AttributeTypeSerializer
    pagination_class = None


class AttributeTypeGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AttributeType.objects.all()
    serializer_class = AttributeTypeSerializer
    pagination_class = None


# ATTRIBUTES
class AddAttributeView(generics.ListCreateAPIView):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    pagination_class = None


class AttributeGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    pagination_class = None


# VARIATION
class AddVariationView(generics.ListCreateAPIView):
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer
    pagination_class = None


class VariationGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer
    pagination_class = None


# HEAD CATEGORY
class AddHeadCategoryView(generics.ListCreateAPIView):
    queryset = HeadCategory.objects.all()
    serializer_class = HeadCategorySerializer
    pagination_class = None


class HeadCategoryGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HeadCategory.objects.all()
    serializer_class = HeadCategorySerializer
    pagination_class = None


# PARENT CATEGORY
class AddParentCategoryView(generics.ListCreateAPIView):
    queryset = ParentCategory.objects.all()
    serializer_class = ParentCategorySerializer
    pagination_class = None


class ParentCategoryGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParentCategory.objects.all()
    serializer_class = ParentCategorySerializer
    pagination_class = None


# CATEGORY
class AddCategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


class CategoryGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


# SUB CATEGORY
class AddSubCategoryView(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    pagination_class = None


class SubCategoryGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    pagination_class = None


# TEMPORARY PRODUCT
class AddTemporaryProductView(generics.ListCreateAPIView):
    queryset = TemporaryProduct.objects.all().order_by('-size')
    serializer_class = TempProductSerializer
    pagination_class = None


class TemporaryProductGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TemporaryProduct.objects.all().order_by('-size')
    serializer_class = TempProductSerializer
    pagination_class = None


# PRODUCT
class AddProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = None


class ProductGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = None

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        delete_stock = Stock.objects.filter(product_name=instance.product_name, sku=instance.sku)
        delete_stock.delete()
        self.perform_destroy(instance)
        return Response(status='200')


# FETCH ALL VARIATION ACCORDING TO ATTRIBUTE AND ITS TYPES
@api_view(['GET'])
def FetchAllAttributeTypeView(request):
    cursor = connections['default'].cursor()
    query = "SELECT att_type from tbl_attribute_type"
    cursor.execute(query)
    all_attribute_type = DictinctFetchAll(cursor)
    return Response(all_attribute_type)


@api_view(['GET'])
def FetchAttributeView(request, code):
    cursor = connections['default'].cursor()
    query = "select attribute_name from tbl_attribute where att_type_id = '" + code + "'"
    cursor.execute(query)
    fetch_attribute = DictinctFetchAll(cursor)
    return Response(fetch_attribute)


@api_view(['GET'])
def FetchlVariationView(request, code):
    cursor = connections['default'].cursor()
    query_employee = "SELECT variation_name, symbol FROM tbl_variation where attribute_name_id = '" + code + "'"
    cursor.execute(query_employee)
    employee_location = DictinctFetchAll(cursor)
    return Response(employee_location)
