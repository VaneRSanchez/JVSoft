from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ProductCategoriesModel(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 20, null = False, blank = False) 
    status = models.BooleanField(default = False, null = False, blank = False)
    
    class Meta: 
        db_table = 'product_categories'
  
class RawMaterialCategoriesModel(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 20, null = False, blank = False) 
    status = models.BooleanField(default = False, null = False, blank = False)
    
    class Meta: 
        db_table = 'raw_material_categories'

class UnitsModel(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 20, null = False, blank = False) 
    
    class Meta: 
        db_table = 'units'

class MovementTypesModel(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 20, null = False, blank = False) 
    
    class Meta: 
        db_table = 'movement_types'

class SalesModel(models.Model):
    id = models.AutoField(primary_key = True)
    total = models.FloatField(default = 0)
    date_reg = models.DateTimeField(default = timezone.now, null = False, blank = False)
    users = models.ForeignKey(User, on_delete = models.RESTRICT)
    
    class Meta: 
        db_table = 'sales'

class ProductsModel(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 20, null = False, blank = False) 
    description = models.CharField(max_length = 150, null = False, blank = False) 
    price = models.FloatField(default = 0)
    status = models.BooleanField(default = False, null = False, blank = False)
    product_categories = models.ForeignKey(ProductCategoriesModel, on_delete = models.RESTRICT)

    class Meta: 
        db_table = 'products'

class RawMaterialsModel(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 20, null = False, blank = False) 
    description = models.CharField(max_length = 20, null = False, blank = False) 
    price = models.FloatField(default = 0)
    status = models.BooleanField(default = False, null = False, blank = False)
    raw_material_categories = models.ForeignKey(RawMaterialCategoriesModel, on_delete = models.RESTRICT)
    units = models.ForeignKey(UnitsModel, on_delete = models.RESTRICT)

    class Meta: 
        db_table = 'raw_materials'

class InventoryRawMaterialsModel(models.Model):
    id = models.AutoField(primary_key = True)
    quantity = models.IntegerField(default = 0, null = False, blank = False)
    date_reg = models.DateTimeField(default = timezone.now, null = False, blank = False)
    date_exp = models.DateTimeField(null = False, blank = False)
    status = models.BooleanField(default = True, null = False, blank = False)
    raw_materials = models.ForeignKey(RawMaterialsModel, on_delete = models.RESTRICT)
    movement_types = models.ForeignKey(MovementTypesModel, on_delete = models.RESTRICT)
    
    class Meta: 
        db_table = 'inventory_raw_materials'

class ProductsMaterialsModel(models.Model):
    id = models.AutoField(primary_key = True)
    quantity = models.FloatField(default = 0, null = False, blank = False)
    products = models.ForeignKey(ProductsModel, on_delete = models.RESTRICT)
    raw_materials = models.ForeignKey(RawMaterialsModel, on_delete = models.RESTRICT)

    class Meta: 
        db_table = 'products_materials'

class DetailSalesModel(models.Model):
    id = models.AutoField(primary_key = True)
    price = models.FloatField(default = 0)
    quantity = models.FloatField(default = 0)
    products = models.ForeignKey(ProductsModel, on_delete = models.RESTRICT)
    sales = models.ForeignKey(SalesModel, on_delete = models.RESTRICT)
    class Meta: 
        db_table = 'detail_sales'