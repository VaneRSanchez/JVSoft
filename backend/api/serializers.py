from rest_framework import serializers
from django.contrib.auth import get_user_model
import api.models as jv_models

class ManageUsersTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'last_login', 'username', 'first_name', 'last_name', 'email', 'is_active', 'date_joined']

class ProductCategoriesAddSerializer(serializers.ModelSerializer):
    name = serializers.CharField(error_messages={
        'required': 'El nombre es requerido. Por favor, proporciona un nombre valido.',
        'blank': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
        'null': 'El nombre no puede estar en blanco. Por favor, proporciona un nombre valido.',
    })

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
    })
    status = serializers.BooleanField(error_messages={
        'required': 'El estatus es requerido. Por favor, proporciona un estatus valido.',
        'blank': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
        'null': 'El estatus no puede estar en blanco. Por favor, proporciona un estatus valido.',
    })

    class Meta:
        model = jv_models.ProductCategoriesModel
        fields = ['id', 'name', 'status']