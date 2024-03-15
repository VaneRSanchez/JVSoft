from django.db import models

class ProductCategoriesModel(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 20, null = False, blank = False) 
    status = models.BooleanField(default = False, null = False, blank = False)
    
    class Meta: 
        db_table = 'product_categories'
