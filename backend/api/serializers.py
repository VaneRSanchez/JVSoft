from rest_framework import serializers
from django.contrib.auth import get_user_model
import api.models as jv_models
from django.db import IntegrityError
from django.db.models import Sum
from django.contrib.auth.models import User

#Productos categorias
class ProductCategoriesTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = jv_models.ProductCategoriesModel
        fields = ['id', 'name', 'status']

class ProductCategoriesAddSerializer(serializers.ModelSerializer):
    name = serializers.CharField(error_messages= {
        'required': 'El nombre es requerido. Por favor, proporciona un nombre valido.',
        'blank': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'null': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'max_length': 'El nombre no puede pasar de los 20 caracteres. Por favor, proporciona un nombre valido.',
    }, max_length = 20)

    class Meta:
        model = jv_models.ProductCategoriesModel
        fields = ['name']

class ProductCategoriesEditSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(error_messages={
        'required': 'El numero de la categoria es requerido. Por favor, proporciona un numero valido.',
        'blank': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'null': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'invalid': 'El numero es invalido. Por favor, proporciona un numero valido.',
    })
    name = serializers.CharField(error_messages={
        'required': 'El nombre es requerido. Por favor, proporciona un nombre valido.',
        'blank': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'null': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'max_length': 'El nombre no puede pasar de los 20 caracteres. Por favor, proporciona un nombre valido.',
    }, max_length = 20)
    status = serializers.BooleanField(error_messages={
        'required': 'El estatus es requerido. Por favor, proporciona un estatus valido.',
        'blank': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
        'null': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
        'invalid': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
    })

    class Meta:
        model = jv_models.ProductCategoriesModel
        fields = ['id', 'name', 'status']

#Materias primas categorias
class RawMaterialCategoriesTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = jv_models.RawMaterialCategoriesModel
        fields = ['id', 'name', 'status']

class RawMaterialCategoriesAddSerializer(serializers.ModelSerializer):
    name = serializers.CharField(error_messages= {
        'required': 'El nombre es requerido. Por favor, proporciona un nombre valido.',
        'blank': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'null': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'max_length': 'El nombre no puede pasar de los 20 caracteres. Por favor, proporciona un nombre valido.',
    }, max_length = 20)

    class Meta:
        model = jv_models.RawMaterialCategoriesModel
        fields = ['name']

class RawMaterialCategoriesEditSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(error_messages={
        'required': 'El numero de la categoria es requerido. Por favor, proporciona un numero valido.',
        'blank': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'null': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'invalid': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',

    })
    name = serializers.CharField(error_messages={
        'required': 'El nombre es requerido. Por favor, proporciona un nombre valido.',
        'blank': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'null': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'max_length': 'El nombre no puede pasar de los 20 caracteres. Por favor, proporciona un nombre valido.',
    }, max_length = 20)
    status = serializers.BooleanField(error_messages={
        'required': 'El estatus es requerido. Por favor, proporciona un estatus valido.',
        'blank': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
        'null': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
        'invalid': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
    })
    
    class Meta:
        model = jv_models.RawMaterialCategoriesModel
        fields = ['id', 'name', 'status']

#Units
class UnitsTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = jv_models.UnitsModel
        fields = ['id', 'name',]

class UnitsAddSerializer(serializers.ModelSerializer):
    name = serializers.CharField(error_messages= {
        'required': 'El nombre es requerido. Por favor, proporciona un nombre valido.',
        'blank': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'null': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'max_length': 'El nombre no puede pasar de los 20 caracteres. Por favor, proporciona un nombre valido.',
    }, max_length = 20)

    class Meta:
        model = jv_models.UnitsModel
        fields = ['name']

class UnitsEditSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(error_messages={
        'required': 'El numero de la categoria es requerido. Por favor, proporciona un numero valido.',
        'blank': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'null': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'invalid': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',

    })
    name = serializers.CharField(error_messages={
        'required': 'El nombre es requerido. Por favor, proporciona un nombre valido.',
        'blank': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'null': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'max_length': 'El nombre no puede pasar de los 20 caracteres. Por favor, proporciona un nombre valido.',
    }, max_length = 20)

    
    class Meta:
        model = jv_models.UnitsModel
        fields = ['id', 'name',]

#Movement types
class MovementTypesTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = jv_models.MovementTypesModel
        fields = ['id', 'name',]

class MovementTypesAddSerializer(serializers.ModelSerializer):
    name = serializers.CharField(error_messages= {
        'required': 'El nombre es requerido. Por favor, proporciona un nombre valido.',
        'blank': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'null': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'max_length': 'El nombre no puede pasar de los 20 caracteres. Por favor, proporciona un nombre valido.',
    }, max_length = 20)

    class Meta:
        model = jv_models.MovementTypesModel
        fields = ['name']

class MovementTypesEditSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(error_messages={
        'required': 'El numero de la categoria es requerido. Por favor, proporciona un numero valido.',
        'blank': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'null': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'invalid': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',

    })
    name = serializers.CharField(error_messages={
        'required': 'El nombre es requerido. Por favor, proporciona un nombre valido.',
        'blank': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'null': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'max_length': 'El nombre no puede pasar de los 20 caracteres. Por favor, proporciona un nombre valido.',
    }, max_length = 20)

    class Meta:
        model = jv_models.MovementTypesModel
        fields = ['id', 'name',]

#User
class UserTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = jv_models.User
        fields = ['username', 'email', 'first_name', 'last_name']

#Products
class ProductsTableSerializer(serializers.ModelSerializer):
    product_categories = ProductCategoriesTableSerializer()

    class Meta:
        model = jv_models.ProductsModel
        fields = ['id','name', 'description', 'price', 'status', 'product_categories']

class ProductsAddSerializer(serializers.ModelSerializer):
    name = serializers.CharField(error_messages= {
        'required': 'El nombre es requerido. Por favor, proporciona un nombre valido.',
        'blank': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'null': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'max_length': 'El nombre no puede pasar de los 20 caracteres. Por favor, proporciona un nombre valido.',
    }, max_length = 20)
    
    description = serializers.CharField(error_messages= {
        'required': 'La descripción es requerida. Por favor, proporciona una descripción valido.',
        'blank': 'La descripción no puede estar en blanco. Por favor, proporciona una descripción valido.',
        'null': 'La descripción no puede estar en blanco. Por favor, proporciona una descripción valido.',
        'max_length': 'La descripción no puede pasar de los 150 caracteres. Por favor, proporciona una descripción valida.',
    }, max_length = 150)

    price = serializers.FloatField(error_messages= {
        'required': 'El precio es requerido. Por favor, proporciona un precio valido.',
        'blank': 'El precio no puede estar en blanco. Por favor, proporciona un precio valido.',
        'null': 'El precio no puede estar en blanco. Por favor, proporciona un precio valido.',
        'invalid': 'El precio es invalido. Por favor, proporciona un precio valido.',
    })

    product_categories_id = serializers.IntegerField(error_messages= {
        'required': 'La categoria de producto es requerido. Por favor, proporciona una categoria de producto valido.',
        'blank': 'La categoria de producto no puede estar en blanco. Por favor, proporciona una categoria de producto valido.',
        'null': 'La categoria de producto no puede estar en blanco. Por favor, proporciona una categoria de producto valido.',
        'invalid': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',

    })

    class Meta:
        model = jv_models.ProductsModel
        fields = ['id', 'name', 'description', 'price', 'product_categories_id']

    def create(self, validated_data):
        try:
            product_categories_id = validated_data.get('product_categories_id')
            if product_categories_id == 0:
                raise serializers.ValidationError({"success": False, "msg": "La categoria de producto es invalido. Por favor, proporciona una categoria de producto valido."})

            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"success": False, "msg": "No se pudo agregar, verifique los datos."})
        
class ProductsEditSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(error_messages={
        'required': 'El id del producto es requerido. Por favor, proporciona un id del producto valido.',
        'blank': 'El id del producto no puede estar en blanco. Por favor, proporciona un id del producto valido.',
        'null': 'El id del producto no puede estar en blanco. Por favor, proporciona un id del producto valido.',
        'invalid': 'El id del producto es invalido. Por favor, proporciona un id del producto valido.',
    })

    name = serializers.CharField(error_messages= {
        'required': 'El nombre es requerido. Por favor, proporciona un nombre valido.',
        'blank': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'null': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'max_length': 'El nombre no puede pasar de los 20 caracteres. Por favor, proporciona un nombre valido.',
    }, max_length = 20)
    
    description = serializers.CharField(error_messages= {
        'required': 'La descripción es requerida. Por favor, proporciona una descripción valido.',
        'blank': 'La descripción no puede estar en blanco. Por favor, proporciona una descripción valido.',
        'null': 'La descripción no puede estar en blanco. Por favor, proporciona una descripción valido.',
        'max_length': 'La descripción no puede pasar de los 150 caracteres. Por favor, proporciona una descripción valida.',
    }, max_length = 150)

    price = serializers.FloatField(error_messages= {
        'required': 'El precio es requerido. Por favor, proporciona un precio valido.',
        'blank': 'El precio no puede estar en blanco. Por favor, proporciona un precio valido.',
        'null': 'El precio no puede estar en blanco. Por favor, proporciona un precio valido.',
        'invalid': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
    })

    status = serializers.BooleanField(error_messages={
        'required': 'El estatus es requerido. Por favor, proporciona un estatus valido.',
        'blank': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
        'null': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
        'invalid': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
    })

    product_categories_id = serializers.IntegerField(error_messages= {
        'required': 'La categoria de producto es requerido. Por favor, proporciona una categoria de producto valido.',
        'blank': 'La categoria de producto no puede estar en blanco. Por favor, proporciona una categoria de producto valido.',
        'null': 'La categoria de producto no puede estar en blanco. Por favor, proporciona una categoria de producto valido.',
        'invalid': 'La categoria es invalida. Por favor, proporciona una categoria valido.',
    })

    class Meta:
        model = jv_models.ProductsModel
        fields = ['id','name','description', 'price','status', 'product_categories_id']

    def create(self, validated_data):
        try:
            product_categories_id = validated_data.get('product_categories_id')
            if product_categories_id == 0:
                raise serializers.ValidationError({"success": False, "msg": "La categoria de producto es invalido. Por favor, proporciona una categoria de producto valido."})

            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"success": False, "msg": "No se pudo agregar, verifique los datos."})
 
#DetailSales
class DetailSalesTableSerializer(serializers.ModelSerializer):
    products = ProductsTableSerializer()

    class Meta:
        model = jv_models.DetailSalesModel
        fields = ['id', 'price', 'quantity', 'products']

class DetailSalesAddSerializer(serializers.ModelSerializer):
    price = serializers.FloatField(error_messages= {
        'required': 'El precio es requerido. Por favor, proporciona un precio valido.',
        'blank': 'El precio no puede estar en blanco. Por favor, proporciona un precio valido.',
        'null': 'El precio no puede estar en blanco. Por favor, proporciona un precio valido.',
        'invalid': 'El precio es invalido. Por favor, proporciona un precio valido.',
    })

    products_id = serializers.IntegerField(error_messages= {
        'required': 'El producto es requerido. Por favor, proporciona un producto valido.',
        'blank': 'El producto no puede estar en blanco. Por favor, proporciona un producto valido.',
        'null': 'El producto no puede estar en blanco. Por favor, proporciona un producto valido.',
        'invalid': 'El producto es invalida. Por favor, proporciona un producto valida.',
    })

    sales_id = serializers.IntegerField(error_messages= {
        'required': 'La venta es requerida. Por favor, proporciona una venta valida.',
        'blank': 'La venta no puede estar en blanco. Por favor, proporciona una venta valida.',
        'null': 'La venta no puede estar en blanco. Por favor, proporciona una venta valida.',
        'invalid': 'La venta es invalida. Por favor, proporciona una venta valida.',
    })

    quantity = serializers.FloatField(error_messages= {
        'required': 'La cantidad es requerida. Por favor, proporciona una cantidad valido.',
        'blank': 'La cantidad no puede estar en blanco. Por favor, proporciona una cantidad valido.',
        'null': 'La cantidad no puede estar en blanco. Por favor, proporciona una cantidad valido.',
        'invalid': 'La cantidad es invalida. Por favor, proporciona una cantidad valida.',
    })

    class Meta:
        model = jv_models.DetailSalesModel
        fields = ['price', 'products_id', 'sales_id', 'quantity']

#Sales
class SalesTableSerializer(serializers.ModelSerializer):
    users = UserTableSerializer()
    detail_sales = serializers.SerializerMethodField()
    
    def get_detail_sales(self, obj):
        detail_sales = jv_models.DetailSalesModel.objects.filter(sales_id=obj.id)
        return DetailSalesTableSerializer(detail_sales, many=True).data

    class Meta:
        model = jv_models.SalesModel
        fields = ['id', 'date_reg', 'total', 'users', 'detail_sales']

class SalesAddSerializer(serializers.ModelSerializer):
    total = serializers.FloatField(error_messages= {
        'required': 'El total es requerido. Por favor, proporciona un nombre valido.',
        'blank': 'El total no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'null': 'El total no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'max_length': 'El total no puede pasar de los 20 caracteres. Por favor, proporciona un nombre valido.',
    })

    class Meta:
        model = jv_models.SalesModel
        fields = ['total']

class SalesEditSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(error_messages={
        'required': 'El numero de la categoria es requerido. Por favor, proporciona un numero valido.',
        'blank': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'null': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'invalid': 'El numero es invalido. Por favor, proporciona un numero valido.',
    })

    total = serializers.CharField(error_messages={
        'required': 'El total es requerido. Por favor, proporciona un nombre valido.',
        'blank': 'El total no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'null': 'El total no puede estar en blanco. Por favor, proporciona un nombre valido.',
    })
    class Meta:
        model = jv_models.SalesModel
        fields = ['id','total']
       
#RawMaterials
class RawMaterialsTableSerializer(serializers.ModelSerializer):
    raw_material_categories = RawMaterialCategoriesTableSerializer()
    units = UnitsTableSerializer()

    class Meta:
        model = jv_models.RawMaterialsModel
        fields = ['id','name', 'description', 'price', 'units', 'raw_material_categories', 'status']

class RawMaterialsAddSerializer(serializers.ModelSerializer):
    name = serializers.CharField(error_messages= {
        'required': 'El nombre es requerido. Por favor, proporciona un nombre valido.',
        'blank': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'null': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'max_length': 'El nombre no puede pasar de los 20 caracteres. Por favor, proporciona un nombre valido.',
    }, max_length = 20)
    
    description = serializers.CharField(error_messages= {
        'required': 'La descripción es requerida. Por favor, proporciona una descripción valido.',
        'blank': 'La descripción no puede estar en blanco. Por favor, proporciona una descripción valido.',
        'null': 'La descripción no puede estar en blanco. Por favor, proporciona una descripción valido.',
        'max_length': 'La descripción no puede pasar de los 20 caracteres. Por favor, proporciona una descripción valida.',
    }, max_length = 150)

    price = serializers.FloatField(error_messages= {
        'required': 'El precio es requerido. Por favor, proporciona un precio valido.',
        'blank': 'El precio no puede estar en blanco. Por favor, proporciona un precio valido.',
        'null': 'El precio no puede estar en blanco. Por favor, proporciona un precio valido.',
        'invalid': 'El precio es invalido. Por favor, proporciona un precio valido.',

    })

    raw_material_categories_id = serializers.IntegerField(error_messages= {
        'required': 'La categoria de la materia prima es requerida. Por favor, proporciona una categoria de la materia prima valida.',
        'blank': 'La categoria de la materia prima no puede estar en blanco. Por favor, proporciona una categoria de la materia prima valida.',
        'null': 'La categoria de la materia prima no puede estar en blanco. Por favor, proporciona una categoria de la materia prima valida.',
        'invalid': 'La categoria de la materia prima es invalida. Por favor, proporciona una categoria de la materia prima valida.',

    })

    units_id = serializers.IntegerField(error_messages= {
        'required': 'La unidad es requerida. Por favor, proporciona una unidad valida.',
        'blank': 'La unidad no puede estar en blanco. Por favor, proporciona una unidad valida.',
        'null': 'La unidad no puede estar en blanco. Por favor, proporciona una unidad valida.',
        'invalid': 'La  unidad es invalida. Por favor, proporciona una unidad valida.',

    })

    raw_material_categories_id = serializers.IntegerField(error_messages= {
        'required': 'La categoria de la materia prima es requerida. Por favor, proporciona una categoria de la materia prima valida.',
        'blank': 'La categoria de la materia prima no puede estar en blanco. Por favor, proporciona una categoria de la materia prima valida.',
        'null': 'La categoria de la materia prima no puede estar en blanco. Por favor, proporciona una categoria de la materia prima valida.',
        'invalid': 'La categoria de la materia prima es invalida. Por favor, proporciona una categoria de la materia prima valida.',
    })

    class Meta:
        model = jv_models.RawMaterialsModel
        fields = ['id', 'name', 'description', 'price', 'raw_material_categories_id', 'units_id']

    def create(self, validated_data):
        try:
            raw_material_categories_id = validated_data.get('raw_material_categories_id')
            if raw_material_categories_id == 0:
                raise serializers.ValidationError({"success": False, "msg": "La categoria de la materia prima es invalido. Por favor, proporciona una categoria de materia prima valido."})

            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"success": False, "msg": "No se pudo agregar, verifique los datos."})
        
class RawMaterialsEditSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(error_messages={
        'required': 'El numero de la categoria es requerido. Por favor, proporciona un numero valido.',
        'blank': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'null': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'invalid': 'El numero de la categoria  es invalida. Por favor, proporciona un numero de la categoria valida.',

    })

    name = serializers.CharField(error_messages= {
        'required': 'El nombre es requerido. Por favor, proporciona un nombre valido.',
        'blank': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'null': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'max_length': 'El nombre no puede pasar de los 20 caracteres. Por favor, proporciona un nombre valido.',
    }, max_length = 20)
    
    description = serializers.CharField(error_messages= {
        'required': 'La descripción es requerida. Por favor, proporciona una descripción valido.',
        'blank': 'La descripción no puede estar en blanco. Por favor, proporciona una descripción valido.',
        'null': 'La descripción no puede estar en blanco. Por favor, proporciona una descripción valido.',
        'max_length': 'La descripción no puede pasar de los 20 caracteres. Por favor, proporciona una descripción valida.',
    }, max_length = 20)

    price = serializers.FloatField(error_messages= {
        'required': 'El precio es requerido. Por favor, proporciona un precio valido.',
        'blank': 'El precio no puede estar en blanco. Por favor, proporciona un precio valido.',
        'null': 'El precio no puede estar en blanco. Por favor, proporciona un precio valido.',
        'invalid': 'El precio es invalido. Por favor, proporciona un precio valido.',

    })

    units_id = serializers.IntegerField(error_messages= {
        'required': 'La unidad es requerida. Por favor, proporciona una unidad valida.',
        'blank': 'La unidad no puede estar en blanco. Por favor, proporciona una unidad valida.',
        'null': 'La unidad no puede estar en blanco. Por favor, proporciona una unidad valida.',
        'invalid': 'La unidad es invalida. Por favor, proporciona una unidad valida.',

    })

    raw_material_categories_id = serializers.IntegerField(error_messages= {
        'required': 'La categoria de la materia prima es requerida. Por favor, proporciona una categoria de la materia prima valida.',
        'blank': 'La categoria de la materia prima no puede estar en blanco. Por favor, proporciona una categoria de la materia prima valida.',
        'null': 'La categoria de la materia prima no puede estar en blanco. Por favor, proporciona una categoria de la materia prima valida.',
        'invalid': 'La categoria de la materia prima es invalida. Por favor, proporciona una categoria de la materia prima valida.',
    })
    
    class Meta:
        model = jv_models.RawMaterialsModel
        fields = ['id','name','description', 'price','units_id', 'raw_material_categories_id']

    def create(self, validated_data):
        try:
            raw_material_categories_id = validated_data.get('raw_material_categories_id')
            if raw_material_categories_id == 0:
                raise serializers.ValidationError({"success": False, "msg": "La categoria de la materia prima es invalida. Por favor, proporciona una categoria de la materia prima valida."})

            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"success": False, "msg": "No se pudo agregar, verifique los datos."})
        
#InventaryRawMaterials
class InventoryRawMaterialsTableSerializer(serializers.ModelSerializer):
    raw_materials = RawMaterialsTableSerializer()
    movement_types = MovementTypesTableSerializer()
    
    class Meta:
        model = jv_models.InventoryRawMaterialsModel
        fields = ['id','quantity', 'date_reg', 'date_exp', 'raw_materials', 'movement_types', 'status']

class InventoryFindRawMaterialsTableSerializer(serializers.ModelSerializer):
    raw_material_categories = RawMaterialCategoriesTableSerializer()
    total_quantity = serializers.SerializerMethodField()

    class Meta:
        model = jv_models.RawMaterialsModel
        fields = ['id','name', 'price', 'raw_material_categories', 'status', 'total_quantity']

    def get_total_quantity(self, obj):
        total_entries = jv_models.InventoryRawMaterialsModel.objects.filter(
            raw_materials = obj,
            movement_types__id = 1,
            status = 1
        ).aggregate(total_entries=Sum('quantity'))['total_entries'] or 0

        total_exits = jv_models.InventoryRawMaterialsModel.objects.filter(
            raw_materials = obj,
            movement_types__id = 2,
            status = 1
        ).aggregate(total_exits=Sum('quantity'))['total_exits'] or 0

        total_quantity = total_entries - total_exits

        return total_quantity
    
class InventoryRawMaterialsAddSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(error_messages= {
        'required': 'La cantidad es requerida. Por favor, proporciona una cantidad valido.',
        'blank': 'La cantidad no puede estar en blanco. Por favor, proporciona una cantidad valido.',
        'null': 'La cantidad no puede estar en blanco. Por favor, proporciona una cantidad valido.',
        'invalid': 'La cantidad es invalida. Por favor, proporciona una cantidad valida.',
    })

    date_exp = serializers.DateTimeField( format='%Y-%m-%dT%H', error_messages= {
        'required': 'La fecha de expiración es requerida. Por favor, proporciona una fecha de expiración valida.',
        'blank': 'fecha de expiración no puede estar en blanco. Por favor, proporciona una fecha de expiración valida.',
        'null': 'fecha de expiración no puede estar en blanco. Por favor, proporciona una fecha de expiración valida.',
        'invalid': 'La fecha de expiración es invalida. Por favor, proporciona una fecha de expiración valid.',
    })

    raw_materials_id = serializers.IntegerField(error_messages= {
        'required': 'La materia prima es requerida. Por favor, proporciona una materia prima  valido.',
        'blank': 'La materia prima no puede estar en blanco. Por favor, proporciona una materia prima valido.',
        'null': 'La materia prima no puede estar en blanco. Por favor, proporciona una materia prima valido.',
        'invalid': 'La materia prima es invalida. Por favor, proporciona una La materia prima valida.',
    })

    movement_types_id = serializers.IntegerField(error_messages= {
        'required': 'El tipo de movimiento es requerido. Por favor, proporciona un tipo de movimiento valido.',
        'blank': 'El tipo de movimiento no puede estar en blanco. Por favor, proporciona un tipo de movimiento valido.',
        'null': 'El tipo de movimiento no puede estar en blanco. Por favor, proporciona un tipo de movimiento valido.',
        'invalid': 'El tipo de movimiento es invalido. Por favor, proporciona un tipo de movimiento valido.',
    })

    class Meta:
        model = jv_models.InventoryRawMaterialsModel
        fields = ['id', 'quantity', 'date_exp', 'raw_materials_id', 'movement_types_id']
    
    def create(self, validated_data):
        try:
            movement_types_id = validated_data.get('movement_types_id')
            if movement_types_id == 0:
                raise serializers.ValidationError({"success": False, "msg": "El tipo de movimiento es invalido. Por favor, proporciona una categoria de materia prima valido."})
            
            raw_materials_id = validated_data.get('raw_materials_id')
            if raw_materials_id == 0:
                raise serializers.ValidationError({"success": False, "msg": "La materia prima es invalida. Por favor, proporciona una materia prima valida."})

            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"success": False, "msg": "No se pudo agregar, verifique los datos."})

class InventoryRawMaterialsCancelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(error_messages={
        'required': 'El numero de la categoria es requerido. Por favor, proporciona un numero valido.',
        'blank': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'null': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'invalid': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero de la categoria valido.',

    })

    status = serializers.BooleanField(error_messages={
        'required': 'El estatus es requerido. Por favor, proporciona un estatus valido.',
        'blank': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
        'null': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
        'invalid': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
    })

    class Meta:
        model = jv_models.InventoryRawMaterialsModel
        fields = ['id', 'status']
    
class InventoryRawMaterialsEditSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(error_messages={
        'required': 'El numero de la categoria es requerido. Por favor, proporciona un numero valido.',
        'blank': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'null': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'invalid': 'El numero de la categoria es invalido. Por favor, proporciona un numero de la categoriavalido.',

    })

    quantity = serializers.IntegerField(error_messages= {
        'required': 'La cantidad es requerida. Por favor, proporciona una cantidad valido.',
        'blank': 'La cantidad no puede estar en blanco. Por favor, proporciona una cantidad valido.',
        'null': 'La cantidad no puede estar en blanco. Por favor, proporciona una cantidad valido.',
        'invalid': 'La cantidad es invalida. Por favor, proporciona una cantidad valida.',
    })

    date_exp = serializers.DateTimeField(error_messages= {
        'required': 'La fecha de expiración es requerida. Por favor, proporciona una fecha de expiración valida.',
        'blank': 'La fecha de expiración no puede estar en blanco. Por favor, proporciona una fecha de expiración valida.',
        'null': 'La fecha de expiración no puede estar en blanco. Por favor, proporciona una fecha de expiración valida.',
        'invalid': 'La fecha de expiración es invalida. Por favor, proporciona una fecha de expiración valida.',
    })

    raw_materials_id = serializers.IntegerField(error_messages= {
        'required': 'La materia prima es requerida. Por favor, proporciona una materia prima  valido.',
        'blank': 'La materia prima no puede estar en blanco. Por favor, proporciona una materia prima valido.',
        'null': 'La materia prima no puede estar en blanco. Por favor, proporciona una materia prima valido.',
        'invalid': 'La materia prima es invalida. Por favor, proporciona una materia prima valida.',
    })

    movement_types_id = serializers.IntegerField(error_messages= {
        'required': 'El tipo de movimiento es requerido. Por favor, proporciona un tipo de movimiento valido.',
        'blank': 'El tipo de movimiento no puede estar en blanco. Por favor, proporciona un tipo de movimiento valido.',
        'null': 'El tipo de movimiento no puede estar en blanco. Por favor, proporciona un tipo de movimiento valido.',
        'invalid': 'El tipo de movimiento es invalido. Por favor, proporciona un tipo de movimiento valido.',
    })
    class Meta:
        model = jv_models.InventoryRawMaterialsModel
        fields = ['id', 'quantity', 'date_exp', 'raw_materials_id', 'movement_types_id']
    
    def create(self, validated_data):
        try:
            movement_types_id = validated_data.get('movement_types_id')
            if movement_types_id == 0:
                raise serializers.ValidationError({"success": False, "msg": "El tipo de movimiento es invalido. Por favor, proporciona una categoria de materia prima valido."})
            
            raw_materials_id = validated_data.get('raw_materials_id')
            if raw_materials_id == 0:
                raise serializers.ValidationError({"success": False, "msg": "La materia prima es invalida. Por favor, proporciona una materia prima valida."})

            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"success": False, "msg": "No se pudo agregar, verifique los datos."})
        
#ProductsMaterials
class ProductsMaterialsTableSerializer(serializers.ModelSerializer):
    products = ProductsTableSerializer()
    raw_materials = RawMaterialsTableSerializer()
    class Meta:
        model = jv_models.ProductsMaterialsModel
        fields = ['id','quantity','products','raw_materials']

class ProductsMaterialsAddSerializer(serializers.ModelSerializer):
    quantity = serializers.FloatField(error_messages= {
        'required': 'La cantidad es requerida. Por favor, proporciona una cantidad valido.',
        'blank': 'La cantidad no puede estar en blanco. Por favor, proporciona una cantidad valido.',
        'null': 'La cantidad no puede estar en blanco. Por favor, proporciona una cantidad valido.',
        'invalid': 'La cantidad es invalida. Por favor, proporciona una cantidad valida.',
    })

    products_id = serializers.IntegerField(error_messages= {
        'required': 'El producto es requerido. Por favor, proporciona un producto valido.',
        'blank': 'El producto no puede estar en blanco. Por favor, proporciona un producto valido.',
        'null': 'El producto no puede estar en blanco. Por favor, proporciona un producto valido.',
        'invalid': 'El producto es invalida. Por favor, proporciona un producto valida.',
    })

    raw_materials_id = serializers.IntegerField(error_messages= {
        'required': 'La materia prima es requerida. Por favor, proporciona una materia prima valida.',
        'blank': 'La materia prima no puede estar en blanco. Por favor, proporciona una materia prima valida.',
        'null': 'La materia prima no puede estar en blanco. Por favor, proporciona una materia prima valida.',
        'invalid': 'La materia prima es invalido. Por favor, proporciona una materia prima valida.',
    })
    class Meta:
        model = jv_models.ProductsMaterialsModel
        fields = ['id', 'quantity', 'raw_materials_id', 'products_id']

class ProductsMaterialsEditSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(error_messages={
        'required': 'El numero de la categoria es requerido. Por favor, proporciona un numero valido.',
        'blank': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'null': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'invalid': 'El numero es invalido. Por favor, proporciona un numero valido.',
    })

    quantity = serializers.IntegerField(error_messages= {
        'required': 'La cantidad es requerida. Por favor, proporciona una cantidad valido.',
        'blank': 'La cantidad no puede estar en blanco. Por favor, proporciona una cantidad valido.',
        'null': 'La cantidad no puede estar en blanco. Por favor, proporciona una cantidad valido.',
        'invalid': 'La cantidad es invalida. Por favor, proporciona una cantidad valida.',
    })

    raw_materials_id = serializers.IntegerField(error_messages= {
        'required': 'La materia prima es requerida. Por favor, proporciona una materia prima  valido.',
        'blank': 'La materia prima no puede estar en blanco. Por favor, proporciona una materia prima valido.',
        'null': 'La materia prima no puede estar en blanco. Por favor, proporciona una materia prima valido.',
        'invalid': 'La materia prima es invalida. Por favor, proporciona una materia prima valida.',
    })

    products_id = serializers.IntegerField(error_messages= {
        'required': 'El producto es requerido. Por favor, proporciona un producto valido.',
        'blank': 'El producto no puede estar en blanco. Por favor, proporciona un producto valido.',
        'null': 'El productono puede estar en blanco. Por favor, proporciona un producto valido.',
        'invalid': 'El producto es invalido. Por favor, proporciona un producto valido.',
    })
    class Meta:
        model = jv_models.ProductsMaterialsModel
        fields = ['id', 'quantity','raw_materials_id', 'products_id']

#SalesFinalize
class SalesFinalizeAddSerializer(serializers.ModelSerializer):
    total = serializers.FloatField(error_messages= {
        'required': 'El total es requerido. Por favor, proporciona un nombre valido.',
        'blank': 'El total no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'null': 'El total no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'max_length': 'El total no puede pasar de los 20 caracteres. Por favor, proporciona un nombre valido.',
    })

    users_id = serializers.IntegerField(error_messages= {
        'required': 'El usuario es requerido. Por favor, proporciona un usuario valido.',
        'blank': 'El usuariono puede estar en blanco. Por favor, proporciona un usuario valido.',
        'null': 'El usuario no puede estar en blanco. Por favor, proporciona un usuario valido.',
        'invalid': 'El usuario es invalido. Por favor, proporciona un usuario valido.',
    })

    class Meta:
        model = jv_models.SalesModel
        fields = ['total', 'users_id']

