from rest_framework import serializers
from AppProduct.models import *
import datetime
from AppCustomer.utils import *
from AppStock.models import *

DateTime = datetime.datetime.now()


# BRAND
class OutletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outlet
        fields = '__all__'

    def create(self, validated_data):
        outlet = super().create(validated_data)
        outlet.updated_at = None
        outlet.created_at = DateTime
        outlet.save()
        return outlet

    def update(self, instance, validated_data):
        outlet = super().update(instance, validated_data)
        outlet.updated_at = DateTime
        outlet.save()
        return outlet


# BRAND
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

    def create(self, validated_data):
        brand = super().create(validated_data)
        brand.updated_at = None
        brand.created_at = DateTime
        brand.save()
        return brand

    def update(self, instance, validated_data):
        brand = super().update(instance, validated_data)
        brand.updated_at = DateTime
        brand.save()
        return brand


# ATTRIBUTE TYPE
class AttributeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeType
        fields = '__all__'

    def create(self, validated_data):
        attr_type = super().create(validated_data)
        attr_type.updated_at = None
        attr_type.created_at = DateTime
        attr_type.save()
        return attr_type

    def update(self, instance, validated_data):
        attr_type = super().update(instance, validated_data)
        attr_type.updated_at = DateTime
        attr_type.save()
        return attr_type


# ATTRIBUTE
class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'

    def create(self, validated_data):
        attribute = super().create(validated_data)
        attribute.updated_at = None
        attribute.created_at = DateTime
        attribute.save()
        return attribute

    def update(self, instance, validated_data):
        attribute = super().update(instance, validated_data)
        attribute.updated_at = DateTime
        attribute.save()
        return attribute


# VARIATION
class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = '__all__'

    def create(self, validated_data):
        variation = super().create(validated_data)
        variation.updated_at = None
        variation.created_at = DateTime
        variation.save()
        return variation

    def update(self, instance, validated_data):
        variation = super().update(instance, validated_data)
        variation.updated_at = DateTime
        variation.save()
        return variation


# HEAD CATEGORY
class HeadCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadCategory
        fields = "__all__"

    def create(self, validated_data):
        h_category = super().create(validated_data)
        h_category.created_at = DateTime
        h_category.updated_at = None
        h_category.save()
        return h_category

    def update(self, instance, validated_data):
        h_category = super().update(instance, validated_data)
        h_category.updated_at = DateTime
        h_category.save()
        return h_category


# PARENT CATEGORY
class ParentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentCategory
        fields = "__all__"

    def create(self, validated_data):
        p_category = super().create(validated_data)
        p_category.created_at = DateTime
        p_category.updated_at = None
        p_category.save()
        return p_category

    def update(self, instance, validated_data):
        p_category = super().update(instance, validated_data)
        p_category.updated_at = DateTime
        p_category.save()
        return p_category


# CATEGORY
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def create(self, validated_data):
        get_subcategory_option = validated_data.get('subcategory_option')
        if get_subcategory_option == 'True':
            validated_data['attribute_name'] = None
        validated_data['created_at'] = DateTime
        validated_data['updated_at'] = None
        category = super().create(validated_data)
        return category

    def update(self, instance, validated_data):

        get_subcategory_option = validated_data.get('subcategory_option')
        if get_subcategory_option == 'True':
            validated_data['attribute_name'] = None
        validated_data['updated_at'] = DateTime
        category = super().update(instance, validated_data)
        return category


# SUB CATEGORY
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

    def create(self, validated_data):
        sub_category = super().create(validated_data)
        sub_category.created_at = DateTime
        sub_category.updated_at = None
        sub_category.save()
        return sub_category

    def update(self, instance, validated_data):
        sub_category = super().update(instance, validated_data)
        sub_category.updated_at = DateTime
        sub_category.save()
        return sub_category


# TEMPORARY PRODUCT
class TempProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemporaryProduct
        fields = '__all__'

    def validate_size(self, value):
        if value == None:
            raise serializers.ValidationError("Please Select Sizes")
        return value

    def create(self, validated_data):
        parent = ''
        used_for_inventory = validated_data.get('used_for_inventory')
        colors = validated_data.get('color')
        colors = colors.replace("'", "")
        colors = colors.replace("[", "")
        colors = colors.replace("]", "")

        sizes = validated_data.get('size')
        sizes = sizes.replace("'", "")
        sizes = sizes.replace("[", "")
        sizes = sizes.replace("]", "")

        split_color = colors.split(",")
        len_color = len(split_color)

        split_size = sizes.split(",")
        len_size = len(split_size)

        if used_for_inventory == 'true':
            if len_color > 0:
                for size in range(len_size):
                    for color in range(len_color):
                        auto_sku_code = AutoGenerateCodeForModel(TemporaryProduct, 'sku', 'PR-')
                        validated_data['sku'] = auto_sku_code
                        validated_data['size'] = split_size[size].strip()
                        validated_data['color'] = split_color[color].strip()
                        parent = super().create(validated_data)

        else:
            if len_size > 0:
                for size in range(len_size):
                    auto_sku_code = AutoGenerateCodeForModel(TemporaryProduct, 'sku', 'PR-')
                    validated_data['sku'] = auto_sku_code
                    validated_data['size'] = split_size[size].strip()
                    validated_data['color'] = 'None'
                    parent = super().create(validated_data)
        return parent

    def update(self, instance, validated_data):
        validated_data['updated_at'] = DateTime
        parent = super().update(instance, validated_data)
        return parent


# PRODUCT
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        parent = ''
        tem_product = TemporaryProduct.objects.all()
        len_tem_product = len(tem_product)
        for x in range(len_tem_product):
            auto_code = AutoGenerateCodeForModel(Product, 'sku', 'PR-')
            validated_data['product_name'] = tem_product[x].product_name
            validated_data['sku'] = auto_code
            validated_data['outlet_name'] = tem_product[x].outlet_name
            validated_data['sub_category_name'] = tem_product[x].sub_category_name
            validated_data['brand_name'] = tem_product[x].brand_name
            validated_data['season'] = tem_product[x].season
            validated_data['description'] = tem_product[x].description
            validated_data['color'] = tem_product[x].color
            validated_data['size'] = tem_product[x].size
            validated_data['image'] = tem_product[x].image
            validated_data['used_for_inventory'] = tem_product[x].used_for_inventory
            validated_data['cost_price'] = tem_product[x].cost_price
            validated_data['selling_price'] = tem_product[x].selling_price
            validated_data['discount_price'] = tem_product[x].discount_price
            validated_data['wholesale_price'] = tem_product[x].wholesale_price
            validated_data['retail_price'] = tem_product[x].retail_price
            validated_data['token_price'] = tem_product[x].token_price
            validated_data['created_at'] = DateTime
            # Add Stock
            add_stock = Stock(
                product_name=tem_product[x].product_name,
                sku=auto_code,
                color=tem_product[x].color,
                size=tem_product[x].size,
                avail_quantity=0,
                created_at=DateTime
            )
            parent = super().create(validated_data)
            add_stock.save()
            tem_product[x].delete()

        return parent

    def update(self, instance, validated_data):
        validated_data['updated_at'] = DateTime
        parent = super().update(instance, validated_data)
        return parent

    # parent = ''
    # used_for_inventory = validated_data.get('used_for_inventory')
    # colors = validated_data.get('color')
    # sizes = validated_data.get('size')
    # split_color = colors.split("^")
    # len_color = len(split_color)
    #
    # split_size = sizes.split("^")
    # len_size = len(split_size)
    #
    # if used_for_inventory == 'true':
    #     if len_color > 0:
    #         for size in range(len_size):
    #             for color in range(len_color):
    #                 validated_data['size'] = split_size[size]
    #                 validated_data['color'] = split_color[color]
    #                 parent = super().create(validated_data)
    # else:
    #     if len_size > 0:
    #         for size in range(len_size):
    #             validated_data['size'] = split_size[size]
    #             parent = super().create(validated_data)
    # return parent
