from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.utils import timezone
from django.core.paginator import Paginator
from django.core.validators import validate_email
from django.db.models import Q
import api.serializers as jv_serializers
import api.models as jv_models
import datetime

class SignInAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]
  
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')              

        if not username:
            return Response({'success': False, 'msg': 'Por favor, proporcione un usuario válido.'}, status = 400)
        elif not password:
            return Response({'success': False, 'msg': 'Por favor, proporcione una contraseña válida.'}, status = 400)
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                'success': True, 
                'msg': 'Redireccionando...',
                'token': access_token
            })
        
        return JsonResponse({'success': False, 'msg': 'Usuario o contraseña incorrecta.'}, status = 401)

class ProductCategoriesAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
  
    def get_object(self, pk):
        try:
            return jv_models.ProductCategoriesModel.objects.get(pk = pk)
        except jv_models.ProductCategoriesModel.DoesNotExist:
            raise JsonResponse({'success': False, 'msg': 'La categoría de producto no existe.'}, status=404)

    def get(self, request):
        query = request.query_params.get('query', '')
        if query == 'table':
            search_query = request.query_params.get('search', '')
            page_number = request.query_params.get('page', 1)
            order_by = request.query_params.get('order_by', 'id')
            order = request.query_params.get('order', 'asc')
            show = request.query_params.get('show', 10)
            
            if order_by == 'actions':
                order_by = 'id'

            product_categories = jv_models.ProductCategoriesModel.objects.filter(
                Q(id__icontains = search_query) |
                Q(name__icontains = search_query) |
                Q(status__icontains = search_query) 
            )

            if order == 'desc':
                order_by = f'-{order_by}'

            product_categories = product_categories.order_by(order_by)
            paginator = Paginator(product_categories, show)
            product_categories_page = paginator.page(page_number)

            serialized = jv_serializers.ProductCategoriesTableSerializer(product_categories_page, many = True)

            return JsonResponse({
                'success': True,
                'data': serialized.data,
                'total_pages': paginator.num_pages,
                'current_page': product_categories_page.number
            })
        elif query == 'info':
            pass
        return JsonResponse({'success': False, 'msg': 'Consulta no encontrada.'}, status=404)
    
    def post(self, request):
        serializer = jv_serializers.ProductCategoriesAddSerializer(data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)
        
        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se agregó correctamente.'}, status = 201)
    
    def put(self, request):
        id = request.data.get('id') 
        instance = self.get_object(id)
        serializer = jv_serializers.ProductCategoriesEditSerializer(instance, data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)

        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se editó correctamente.'}, status = 200)
    
class RawMaterialCategoriesAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
  
    def get_object(self, pk):
        try:
            return jv_models.RawMaterialCategoriesModel.objects.get(pk = pk)
        except jv_models.RawMaterialCategoriesModel.DoesNotExist:
            raise JsonResponse({'success': False, 'msg': 'La categoría de la materia prima no existe.'}, status = 404)

    def get(self, request):
        query = request.query_params.get('query', '')
        if query == 'table':
            search_query = request.query_params.get('search', '')
            page_number = request.query_params.get('page', 1)
            order_by = request.query_params.get('order_by', 'id')
            order = request.query_params.get('order', 'asc')
            show = request.query_params.get('show', 10)
            
            if order_by == 'actions':
                order_by = 'id'

            raw_material_categories = jv_models.RawMaterialCategoriesModel.objects.filter(
                Q(id__icontains = search_query) |
                Q(name__icontains = search_query) |
                Q(status__icontains = search_query) 
            )

            if order == 'desc':
                order_by = f'-{order_by}'

            raw_material_categories = raw_material_categories.order_by(order_by)
            paginator = Paginator(raw_material_categories, show)
            raw_material_categories_page = paginator.page(page_number)

            serialized = jv_serializers.RawMaterialCategoriesTableSerializer(raw_material_categories_page, many = True)

            return JsonResponse({
                'success': True,
                'data': serialized.data,
                'total_pages': paginator.num_pages,
                'current_page': raw_material_categories_page.number
            })
        elif query == 'info':
            pass
        return JsonResponse({'success': False, 'msg': 'Consulta no encontrada.'}, status=404)
    
    def post(self, request):
        serializer = jv_serializers.RawMaterialCategoriesAddSerializer(data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)
        
        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se agregó correctamente.'}, status = 201)
    
    def put(self, request):
        id = request.data.get('id') 
        instance = self.get_object(id)
        serializer = jv_serializers.RawMaterialCategoriesEditSerializer(instance, data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)

        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se editó correctamente.'}, status = 200)
    
class UnitsAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
  
    def get_object(self, pk):
        try:
            return jv_models.UnitsModel.objects.get(pk = pk)
        except jv_models.RawMaterialCategoriesModel.DoesNotExist:
            raise JsonResponse({'success': False, 'msg': 'La unidad no existe.'}, status = 404)

    def get(self, request):
        query = request.query_params.get('query', '')
        if query == 'table':
            search_query = request.query_params.get('search', '')
            page_number = request.query_params.get('page', 1)
            order_by = request.query_params.get('order_by', 'id')
            order = request.query_params.get('order', 'asc')
            show = request.query_params.get('show', 10)
            
            if order_by == 'actions':
                order_by = 'id'

            units = jv_models.UnitsModel.objects.filter(
                Q(id__icontains = search_query) |
                Q(name__icontains = search_query)
            )

            if order == 'desc':
                order_by = f'-{order_by}'

            units = units.order_by(order_by)
            paginator = Paginator(units, show)
            units_page = paginator.page(page_number)

            serialized = jv_serializers.UnitsTableSerializer(units_page, many = True)

            return JsonResponse({
                'success': True,
                'data': serialized.data,
                'total_pages': paginator.num_pages,
                'current_page': units_page.number
            })
        elif query == 'info':
            pass
        return JsonResponse({'success': False, 'msg': 'Consulta no encontrada.'}, status=404)
    
    def post(self, request):
        serializer = jv_serializers.UnitsAddSerializer(data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)
        
        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se agregó correctamente.'}, status = 201)
    
    def put(self, request):
        id = request.data.get('id') 
        instance = self.get_object(id)
        serializer = jv_serializers.UnitsEditSerializer(instance, data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)

        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se editó correctamente.'}, status = 200)

class MovementTypesAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
  
    def get_object(self, pk):
        try:
            return jv_models.MovementTypesModel.objects.get(pk = pk)
        except jv_models.MovementTypesModel.DoesNotExist:
            raise JsonResponse({'success': False, 'msg': 'El tipo de movimiento no existe.'}, status = 404)

    def get(self, request):
        query = request.query_params.get('query', '')
        if query == 'table':
            search_query = request.query_params.get('search', '')
            page_number = request.query_params.get('page', 1)
            order_by = request.query_params.get('order_by', 'id')
            order = request.query_params.get('order', 'asc')
            show = request.query_params.get('show', 10)
            
            if order_by == 'actions':
                order_by = 'id'

            movement_types = jv_models.MovementTypesModel.objects.filter(
                Q(id__icontains = search_query) |
                Q(name__icontains = search_query)
            )

            if order == 'desc':
                order_by = f'-{order_by}'

            movement_types = movement_types.order_by(order_by)
            paginator = Paginator(movement_types, show)
            movement_types_page = paginator.page(page_number)

            serialized = jv_serializers.MovementTypesTableSerializer(movement_types_page, many = True)

            return JsonResponse({
                'success': True,
                'data': serialized.data,
                'total_pages': paginator.num_pages,
                'current_page': movement_types_page.number
            })
        elif query == 'info':
            pass
        return JsonResponse({'success': False, 'msg': 'Consulta no encontrada.'}, status=404)
    
    def post(self, request):
        serializer = jv_serializers.MovementTypesAddSerializer(data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)
        
        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se agregó correctamente.'}, status = 201)
    
    def put(self, request):
        id = request.data.get('id') 
        instance = self.get_object(id)
        serializer = jv_serializers.MovementTypesEditSerializer(instance, data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)

        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se editó correctamente.'}, status = 200)
    
class SalesAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
  
    def get_object(self, pk):
        try:
            return jv_models.SalesModel.objects.get(pk = pk)
        except jv_models.SalesModel.DoesNotExist:
            raise JsonResponse({'success': False, 'msg': 'La venta no existe.'}, status = 404)

    def get(self, request):
        query = request.query_params.get('query', '')
        if query == 'table':
            search_query = request.query_params.get('search', '')
            page_number = request.query_params.get('page', 1)
            order_by = request.query_params.get('order_by', 'id')
            order = request.query_params.get('order', 'asc')
            show = request.query_params.get('show', 10)
            
            if order_by == 'actions':
                order_by = 'id'

            sales = jv_models.SalesModel.objects.filter(
                Q(id__icontains = search_query) |
                Q(total__icontains = search_query)
            )

            if order == 'desc':
                order_by = f'-{order_by}'

            sales = sales.order_by(order_by)
            paginator = Paginator(sales, show)
            sales_page = paginator.page(page_number)

            serialized = jv_serializers.SalesTableSerializer(sales_page, many = True)

            return JsonResponse({
                'success': True,
                'data': serialized.data,
                'total_pages': paginator.num_pages,
                'current_page': sales_page.number
            })
        elif query == 'info':
            pass
        return JsonResponse({'success': False, 'msg': 'Consulta no encontrada.'}, status=404)
    
    def post(self, request):
        serializer = jv_serializers.SalesAddSerializer(data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)
        
        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se agregó correctamente.'}, status = 201)
    
    def put(self, request):
        id = request.data.get('id') 
        instance = self.get_object(id)
        serializer = jv_serializers.SalesEditSerializer(instance, data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)

        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se editó correctamente.'}, status = 200)

class ProductsAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
  
    def get_object(self, pk):
        try:
            return jv_models.ProductsModel.objects.get(pk = pk)
        except jv_models.ProductsModel.DoesNotExist:
            raise JsonResponse({'success': False, 'msg': 'El producto no existe.'}, status = 404)

    def get(self, request):
        query = request.query_params.get('query', '')
        if query == 'table':
            search_query = request.query_params.get('search', '')
            page_number = request.query_params.get('page', 1)
            order_by = request.query_params.get('order_by', 'id')
            order = request.query_params.get('order', 'asc')
            show = request.query_params.get('show', 10)
            
            if order_by == 'actions':
                order_by = 'id'

            products = jv_models.ProductsModel.objects.filter(
                Q(id__icontains = search_query) |
                Q(name__icontains = search_query) |
                Q(description__icontains = search_query)|
                Q(price__icontains = search_query) |
                Q(status__icontains = search_query) 
            )

            if order == 'desc':
                order_by = f'-{order_by}'

            products = products.order_by(order_by)
            paginator = Paginator(products, show)
            products_page = paginator.page(page_number)

            serialized = jv_serializers.ProductsTableSerializer(products_page, many = True)

            return JsonResponse({
                'success': True,
                'data': serialized.data,
                'total_pages': paginator.num_pages,
                'current_page': products_page.number
            })
        elif query == 'info':
            pass
        return JsonResponse({'success': False, 'msg': 'Consulta no encontrada.'}, status=404)
    
    def post(self, request):
        serializer = jv_serializers.ProductsAddSerializer(data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)
        
        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se agregó correctamente.'}, status = 201)
    
    def put(self, request):
        id = request.data.get('id') 
        instance = self.get_object(id)
        serializer = jv_serializers.ProductsEditSerializer(instance, data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)

        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se editó correctamente.'}, status = 200)

class RawMaterialsAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
  
    def get_object(self, pk):
        try:
            return jv_models.RawMaterialsModel.objects.get(pk = pk)
        except jv_models.RawMaterialsModel.DoesNotExist:
            raise JsonResponse({'success': False, 'msg': 'La materia prima no existe.'}, status = 404)

    def get(self, request):
        query = request.query_params.get('query', '')
        if query == 'table':
            search_query = request.query_params.get('search', '')
            page_number = request.query_params.get('page', 1)
            order_by = request.query_params.get('order_by', 'id')
            order = request.query_params.get('order', 'asc')
            show = request.query_params.get('show', 10)
            
            if order_by == 'actions':
                order_by = 'id'

            raw_materials = jv_models.RawMaterialsModel.objects.filter(
                Q(id__icontains = search_query) |
                Q(name__icontains = search_query) |
                Q(description__icontains = search_query)|
                Q(price__icontains = search_query) |
                Q(status__icontains = search_query) 
            )

            if order == 'desc':
                order_by = f'-{order_by}'

            raw_materials = raw_materials.order_by(order_by)
            paginator = Paginator(raw_materials, show)
            raw_materials_page = paginator.page(page_number)

            serialized = jv_serializers.RawMaterialsTableSerializer(raw_materials_page, many = True)

            return JsonResponse({
                'success': True,
                'data': serialized.data,
                'total_pages': paginator.num_pages,
                'current_page': raw_materials_page.number
            })
        elif query == 'info':
            pass
        return JsonResponse({'success': False, 'msg': 'Consulta no encontrada.'}, status=404)
    
    def post(self, request):
        serializer = jv_serializers.RawMaterialsAddSerializer(data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)
        
        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se agregó correctamente.'}, status = 201)
    
    def put(self, request):
        id = request.data.get('id') 
        instance = self.get_object(id)
        serializer = jv_serializers.RawMaterialsEditSerializer(instance, data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)

        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se editó correctamente.'}, status = 200)

class InventaryRawMaterialsAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
  
    def get_object(self, pk):
        try:
            return jv_models.InventaryRawMaterialsModel.objects.get(pk = pk)
        except jv_models.InventaryRawMaterialsModel.DoesNotExist:
            raise JsonResponse({'success': False, 'msg': 'El inventario de la materia prima no existe.'}, status = 404)

    def get(self, request):
        query = request.query_params.get('query', '')
        if query == 'table':
            search_query = request.query_params.get('search', '')
            page_number = request.query_params.get('page', 1)
            order_by = request.query_params.get('order_by', 'id')
            order = request.query_params.get('order', 'asc')
            show = request.query_params.get('show', 10)
            
            if order_by == 'actions':
                order_by = 'id'

            inventary_raw_materials = jv_models.InventaryRawMaterialsModel.objects.filter(
                Q(id__icontains = search_query) |
                Q(quantity__icontains = search_query) |
                Q(date_reg__icontains = search_query)|
                Q(date_exp__icontains = search_query)
            )

            if order == 'desc':
                order_by = f'-{order_by}'

            inventary_raw_materials = inventary_raw_materials.order_by(order_by)
            paginator = Paginator(inventary_raw_materials, show)
            inventary_raw_materials_page = paginator.page(page_number)

            serialized = jv_serializers.InventaryRawMaterialsTableSerializer(inventary_raw_materials_page, many = True)

            return JsonResponse({
                'success': True,
                'data': serialized.data,
                'total_pages': paginator.num_pages,
                'current_page': inventary_raw_materials_page.number
            })
        elif query == 'info':
            pass
        return JsonResponse({'success': False, 'msg': 'Consulta no encontrada.'}, status=404)
    
    def post(self, request):
        serializer = jv_serializers.InventaryRawMaterialsAddSerializer(data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)
        
        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se agregó correctamente.'}, status = 201)
    
    def put(self, request):
        id = request.data.get('id') 
        instance = self.get_object(id)
        serializer = jv_serializers.InventaryRawMaterialsEditSerializer(instance, data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)

        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se editó correctamente.'}, status = 200)

class ProductsMateriaAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
  
    def get_object(self, pk):
        try:
            return jv_models.ProductsMateriaModel.objects.get(pk = pk)
        except jv_models.ProductsMateriaModel.DoesNotExist:
            raise JsonResponse({'success': False, 'msg': 'El producto de la materia prima no existe.'}, status = 404)

    def get(self, request):
        query = request.query_params.get('query', '')
        if query == 'table':
            search_query = request.query_params.get('search', '')
            page_number = request.query_params.get('page', 1)
            order_by = request.query_params.get('order_by', 'id')
            order = request.query_params.get('order', 'asc')
            show = request.query_params.get('show', 10)
            
            if order_by == 'actions':
                order_by = 'id'

            products_materia = jv_models.ProductsMateriaModel.objects.filter(
                Q(id__icontains = search_query) |
                Q(quantity__icontains = search_query) 
            )

            if order == 'desc':
                order_by = f'-{order_by}'

            products_materia = products_materia.order_by(order_by)
            paginator = Paginator(products_materia, show)
            products_materia_page = paginator.page(page_number)

            serialized = jv_serializers.ProductsMateriaTableSerializer(products_materia_page, many = True)

            return JsonResponse({
                'success': True,
                'data': serialized.data,
                'total_pages': paginator.num_pages,
                'current_page': products_materia_page.number
            })
        elif query == 'info':
            pass
        return JsonResponse({'success': False, 'msg': 'Consulta no encontrada.'}, status=404)
    
    def post(self, request):
        serializer = jv_serializers.ProductsMateriaAddSerializer(data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)
        
        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se agregó correctamente.'}, status = 201)
    
    def put(self, request):
        id = request.data.get('id') 
        instance = self.get_object(id)
        serializer = jv_serializers.ProductsMateriaEditSerializer(instance, data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)

        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se editó correctamente.'}, status = 200)

class DetailSalesAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
  
    def get_object(self, pk):
        try:
            return jv_models.DetailSalesModel.objects.get(pk = pk)
        except jv_models.DetailSalesModel.DoesNotExist:
            raise JsonResponse({'success': False, 'msg': 'El detalle de venta no existe.'}, status = 404)

    def get(self, request):
        query = request.query_params.get('query', '')
        if query == 'table':
            search_query = request.query_params.get('search', '')
            page_number = request.query_params.get('page', 1)
            order_by = request.query_params.get('order_by', 'id')
            order = request.query_params.get('order', 'asc')
            show = request.query_params.get('show', 10)
            
            if order_by == 'actions':
                order_by = 'id'

            products_materia = jv_models.DetailSalesModel.objects.filter(
                Q(id__icontains = search_query) |
                Q(price__icontains = search_query) |
                Q(data_reg__icontains = search_query) 

            )

            if order == 'desc':
                order_by = f'-{order_by}'

            detail_sales = detail_sales.order_by(order_by)
            paginator = Paginator(detail_sales, show)
            detail_sales_page = paginator.page(page_number)

            serialized = jv_serializers.DetailSalesTableSerializer(detail_sales_page, many = True)

            return JsonResponse({
                'success': True,
                'data': serialized.data,
                'total_pages': paginator.num_pages,
                'current_page': detail_sales_page.number
            })
        elif query == 'info':
            pass
        return JsonResponse({'success': False, 'msg': 'Consulta no encontrada.'}, status=404)
    
    def post(self, request):
        serializer = jv_serializers.DetailSalesAddSerializer(data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)
        
        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se agregó correctamente.'}, status = 201)
    
    def put(self, request):
        id = request.data.get('id') 
        instance = self.get_object(id)
        serializer = jv_serializers.DetailSalesEditSerializer(instance, data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)

        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se editó correctamente.'}, status = 200)