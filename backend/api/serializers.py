from rest_framework import serializers
from django.contrib.auth import get_user_model
import api.models as jv_models
from django.db import IntegrityError

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
        'valid': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
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
        'valid': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
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

#Sales
class SalesTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = jv_models.SalesModel
        fields = ['id','total']

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
    })

    total = serializers.CharField(error_messages={
        'required': 'El total es requerido. Por favor, proporciona un nombre valido.',
        'blank': 'El total no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'null': 'El total no puede estar en blanco. Por favor, proporciona un nombre valido.',
    })
    class Meta:
        model = jv_models.SalesModel
        fields = ['id','total']

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
        'max_length': 'La descripción no puede pasar de los 20 caracteres. Por favor, proporciona una descripción valida.',
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
        'required': 'El numero de la categoria es requerido. Por favor, proporciona un numero valido.',
        'blank': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'null': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
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
    })

    status = serializers.BooleanField(error_messages={
        'required': 'El estatus es requerido. Por favor, proporciona un estatus valido.',
        'blank': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
        'null': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
        'valid': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
    })

    
    class Meta:
        model = jv_models.ProductsModel
        fields = ['id','name','description', 'price']

#RawMaterials
class RawMaterialsTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = jv_models.RawMaterialsModel
        fields = ['id','name', 'description', 'price', 'status']

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
    })

    raw_material_categories_id = serializers.IntegerField(error_messages= {
        'required': 'La categoria de producto es requerido. Por favor, proporciona una categoria de producto valido.',
        'blank': 'La categoria de producto no puede estar en blanco. Por favor, proporciona una categoria de producto valido.',
        'null': 'La categoria de producto no puede estar en blanco. Por favor, proporciona una categoria de producto valido.',
    })

    units_id = serializers.IntegerField(error_messages= {
        'required': 'La categoria de producto es requerido. Por favor, proporciona una categoria de producto valido.',
        'blank': 'La categoria de producto no puede estar en blanco. Por favor, proporciona una categoria de producto valido.',
        'null': 'La categoria de producto no puede estar en blanco. Por favor, proporciona una categoria de producto valido.',
    })
    class Meta:
        model = jv_models.RawMaterialsModel
        fields = ['id', 'name', 'description', 'price', 'raw_material_categories_id', 'units_id']

class RawMaterialsEditSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(error_messages={
        'required': 'El numero de la categoria es requerido. Por favor, proporciona un numero valido.',
        'blank': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'null': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
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
    })

    status = serializers.BooleanField(error_messages={
        'required': 'El estatus es requerido. Por favor, proporciona un estatus valido.',
        'blank': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
        'null': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
        'invalid': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
    })

    
    class Meta:
        model = jv_models.RawMaterialsModel
        fields = ['id','name','description', 'price']

#InventaryRawMaterials
class InventaryRawMaterialsTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = jv_models.InventaryRawMaterialsModel
        fields = ['id','quantity', 'date_reg', 'date_exp']

class InventaryRawMaterialsAddSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(error_messages= {
        'required': 'La cantidad es requerida. Por favor, proporciona una cantidad valido.',
        'blank': 'La cantidad no puede estar en blanco. Por favor, proporciona una cantidad valido.',
        'null': 'La cantidad no puede estar en blanco. Por favor, proporciona una cantidad valido.',
        'invalid': 'El precio es invalido. Por favor, proporciona un precio valido.',
    })

    data_exp = serializers.DateTimeField(error_messages= {
        'required': 'La fecha de expiración es requerida. Por favor, proporciona una fecha de expiración valida.',
        'blank': 'fecha de expiración no puede estar en blanco. Por favor, proporciona una fecha de expiración valida.',
        'null': 'fecha de expiración no puede estar en blanco. Por favor, proporciona una fecha de expiración valida.',
        'invalid': 'El precio es invalido. Por favor, proporciona un precio valido.',
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
        model = jv_models.InventaryRawMaterialsModel
        fields = ['id', 'quantity', 'data_exp', 'raw_materials_id', 'movement_types_id']

class InventaryRawMaterialsEditSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(error_messages={
        'required': 'El numero de la categoria es requerido. Por favor, proporciona un numero valido.',
        'blank': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'null': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
    })

    quantity = serializers.IntegerField(error_messages= {
        'required': 'La cantidad es requerida. Por favor, proporciona una cantidad valido.',
        'blank': 'La cantidad no puede estar en blanco. Por favor, proporciona una cantidad valido.',
        'null': 'La cantidad no puede estar en blanco. Por favor, proporciona una cantidad valido.',
        'invalid': 'La cantidad es invalida. Por favor, proporciona una cantidad valida.',
    })

    data_exp = serializers.DateTimeField(error_messages= {
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
        model = jv_models.InventaryRawMaterialsModel
        fields = ['id', 'quantity', 'data_exp', 'raw_materials_id', 'movement_types_id']

#ProductsMateria
class ProductsMateriaTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = jv_models.ProductsMateriaModel
        fields = ['id','quantity']

class ProductsMateriaAddSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(error_messages= {
        'required': 'La cantidad es requerida. Por favor, proporciona una cantidad valido.',
        'blank': 'La cantidad no puede estar en blanco. Por favor, proporciona una cantidad valido.',
        'null': 'La cantidad no puede estar en blanco. Por favor, proporciona una cantidad valido.',
        'invalid': 'El precio es invalido. Por favor, proporciona un precio valido.',
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
        model = jv_models.ProductsMateriaModel
        fields = ['id', 'quantity', 'raw_materials_id', 'products_id']

class ProductsMateriaEditSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(error_messages={
        'required': 'El numero de la categoria es requerido. Por favor, proporciona un numero valido.',
        'blank': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'null': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
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

    product_id = serializers.IntegerField(error_messages= {
        'required': 'El producto es requerido. Por favor, proporciona un producto valido.',
        'blank': 'El producto no puede estar en blanco. Por favor, proporciona un producto valido.',
        'null': 'El productono puede estar en blanco. Por favor, proporciona un producto valido.',
        'invalid': 'El productoes invalido. Por favor, proporciona un producto valido.',
    })
    class Meta:
        model = jv_models.InventaryRawMaterialsModel
        fields = ['id', 'quantity', 'data_exp', 'raw_materials_id', 'product_id']

#DetailSales
class DetailSalesTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = jv_models.DetailSalesModel
        fields = ['id','price', 'date_reg']

class DetailSalesAddSerializer(serializers.ModelSerializer):
    price = serializers.FloatField(error_messages= {
        'required': 'El precio es requerido. Por favor, proporciona un precio valido.',
        'blank': 'El precio no puede estar en blanco. Por favor, proporciona un precio valido.',
        'null': 'El precio no puede estar en blanco. Por favor, proporciona un precio valido.',
        'invalid': 'El precio es invalido. Por favor, proporciona un precio valido.',
    })

    data_reg = serializers.DateTimeField(error_messages= {
        'required': 'La fecha de registro es requerida. Por favor, proporciona una fecha de registro valida.',
        'blank': 'fecha de registro no puede estar en blanco. Por favor, proporciona una fecha de registro valida.',
        'null': 'fecha de registro no puede estar en blanco. Por favor, proporciona una fecha de registro valida.',
        'invalid': 'El registro es invalido. Por favor, proporciona un precio valido.',
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

    users_id = serializers.IntegerField(error_messages= {
        'required': 'El usuario es requerido. Por favor, proporciona un usuario valido.',
        'blank': 'El usuariono puede estar en blanco. Por favor, proporciona un usuario valido.',
        'null': 'El usuario no puede estar en blanco. Por favor, proporciona un usuario valido.',
        'invalid': 'El usuario es invalido. Por favor, proporciona un usuario valido.',
    })

    class Meta:
        model = jv_models.DetailSalesModel
        fields = ['id', 'price', 'users_id', 'products_id', 'sales_id']

class DetailSalesEditSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(error_messages={
        'required': 'El numero de la categoria es requerido. Por favor, proporciona un numero valido.',
        'blank': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
        'null': 'El numero de la categoria no puede estar en blanco. Por favor, proporciona un numero valido.',
    })

    price = serializers.FloatField(error_messages= {
        'required': 'El precio es requerido. Por favor, proporciona un precio valido.',
        'blank': 'El precio no puede estar en blanco. Por favor, proporciona un precio valido.',
        'null': 'El precio no puede estar en blanco. Por favor, proporciona un precio valido.',
        'invalid': 'El precio es invalido. Por favor, proporciona un precio valido.',
    })

    data_reg = serializers.DateTimeField(error_messages= {
        'required': 'La fecha de registro es requerida. Por favor, proporciona una fecha de registro valida.',
        'blank': 'fecha de registro no puede estar en blanco. Por favor, proporciona una fecha de registro valida.',
        'null': 'fecha de registro no puede estar en blanco. Por favor, proporciona una fecha de registro valida.',
        'invalid': 'El registro es invalido. Por favor, proporciona un precio valido.',
    })

    product_id = serializers.IntegerField(error_messages= {
        'required': 'El producto es requerido. Por favor, proporciona un producto valido.',
        'blank': 'El producto no puede estar en blanco. Por favor, proporciona un producto valido.',
        'null': 'El productono puede estar en blanco. Por favor, proporciona un producto valido.',
        'invalid': 'El productoes invalido. Por favor, proporciona un producto valido.',
    })

    sales_id = serializers.IntegerField(error_messages= {
        'required': 'La venta es requerida. Por favor, proporciona una venta valida.',
        'blank': 'La venta no puede estar en blanco. Por favor, proporciona una venta valida.',
        'null': 'La venta no puede estar en blanco. Por favor, proporciona una venta valida.',
        'invalid': 'La venta es invalida. Por favor, proporciona una venta valida.',
    })

    users_id = serializers.IntegerField(error_messages= {
        'required': 'El usuario es requerido. Por favor, proporciona un usuario valido.',
        'blank': 'El usuariono puede estar en blanco. Por favor, proporciona un usuario valido.',
        'null': 'El usuario no puede estar en blanco. Por favor, proporciona un usuario valido.',
        'invalid': 'El usuario es invalido. Por favor, proporciona un usuario valido.',
    })
    class Meta:
        model = jv_models.DetailSalesModel
        fields = ['id', 'price', 'data_reg', 'sales_id', 'product_id', 'users_id']