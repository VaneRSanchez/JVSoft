from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import JsonResponse, Http404
from django.template.loader import get_template
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Q 
import api.serializers as jv_serializers
import api.models as jv_models

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
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
  
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
        elif query == 'statistics':
            count_total = jv_models.ProductCategoriesModel.objects.filter(
            ).count()

            count_active = jv_models.ProductCategoriesModel.objects.filter(
                status = 1
            ).count()

            count_hidden = jv_models.ProductCategoriesModel.objects.filter(
                status = 0
            ).count()

            return JsonResponse({
                'success': True,
                'count_total': count_total,
                'count_active': count_active,
                'count_hidden': count_hidden,
            })
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
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
  
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
        elif query == 'statistics':
            count_total = jv_models.RawMaterialCategoriesModel.objects.filter(
            ).count()

            count_active = jv_models.RawMaterialCategoriesModel.objects.filter(
                status = 1
            ).count()

            count_hidden = jv_models.RawMaterialCategoriesModel.objects.filter(
                status = 0
            ).count()

            return JsonResponse({
                'success': True,
                'count_total': count_total,
                'count_active': count_active,
                'count_hidden': count_hidden,
            })
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
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
  
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
        elif query == 'statistics':
            count_total= jv_models.UnitsModel.objects.filter(
            ).count()

            return JsonResponse({
                'success': True,
                'count_total': count_total
            })
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
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
  
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
        elif query == 'statistics':

            count_total = jv_models.MovementTypesModel.objects.filter(
            ).count()

            return JsonResponse({
                'success': True,
                'count_total': count_total,
            })
        
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
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
  
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
        elif query == 'obj':
            id = request.query_params.get('id', None)
            instance = self.get_object(id)
            serialized = jv_serializers.SalesTableSerializer(instance)
            return JsonResponse({
                'success': True,
                'data': serialized.data,
            })
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
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
  
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
                Q(status__icontains = search_query) |
                Q(product_categories__name__icontains=search_query)
            )

            if order_by == 'product_categories.name':
                order_by = 'product_categories__name'

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
        elif query == 'statistics':

            count_total = jv_models.ProductsModel.objects.filter(
            ).count()

            count_active = jv_models.ProductsModel.objects.filter(
                status = 1
            ).count()

            count_hidden = jv_models.ProductsModel.objects.filter(
                status = 0
            ).count()


            return JsonResponse({
                'success': True,
                'count_total': count_total,
                'count_active': count_active,
                'count_hidden': count_hidden,
            })
        
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
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
  
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
        elif query == 'statistics':
            count_total = jv_models.RawMaterialsModel.objects.filter(
            ).count()

            count_active = jv_models.RawMaterialsModel.objects.filter(
                status = 1
            ).count()

            count_hidden = jv_models.RawMaterialsModel.objects.filter(
                status = 0
            ).count()

            return JsonResponse({
                'success': True,
                'count_total': count_total,
                'count_active': count_active,
                'count_hidden': count_hidden,
            })
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

class InventoryRawMaterialsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
  
    def get_object(self, pk):
        try:
            return jv_models.InventoryRawMaterialsModel.objects.get(pk = pk)
        except jv_models.InventoryRawMaterialsModel.DoesNotExist:
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

            inventory_raw_materials = jv_models.InventoryRawMaterialsModel.objects.filter(
                Q(id__icontains = search_query) |
                Q(quantity__icontains = search_query) |
                Q(date_reg__icontains = search_query)|
                Q(date_exp__icontains = search_query)
            )

            if order == 'desc':
                order_by = f'-{order_by}'

            inventory_raw_materials = inventory_raw_materials.order_by(order_by)
            paginator = Paginator(inventory_raw_materials, show)
            inventory_raw_materials_page = paginator.page(page_number)

            serialized = jv_serializers.InventoryRawMaterialsTableSerializer(inventory_raw_materials_page, many = True)

            return JsonResponse({
                'success': True,
                'data': serialized.data,
                'total_pages': paginator.num_pages,
                'current_page': inventory_raw_materials_page.number
            })
        elif query == 'table_raw_materials':
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

            serialized = jv_serializers.InventoryFindRawMaterialsTableSerializer(raw_materials_page, many = True)

            return JsonResponse({
                'success': True,
                'data': serialized.data,
                'total_pages': paginator.num_pages,
                'current_page': raw_materials_page.number
            })
        elif query == 'statistics':
            current_date = timezone.now().date()
            two_days = current_date + timedelta(days=2)

            count_movements = jv_models.InventoryRawMaterialsModel.objects.filter(
            ).count()

            count_raw_materials_expiration = jv_models.InventoryRawMaterialsModel.objects.filter(
                date_exp__gt = current_date, 
                date_exp__lte = two_days,
                status = 1
            ).count()

            count_raw_materials_expired = jv_models.InventoryRawMaterialsModel.objects.filter(
                date_exp__lte = current_date,
                status = 1
            ).count()


            return JsonResponse({
                'success': True,
                'count_movements': count_movements,
                'count_raw_materials_expiration': count_raw_materials_expiration,
                'count_raw_materials_expired': count_raw_materials_expired,
            })
        
        return JsonResponse({'success': False, 'msg': 'Consulta no encontrada.'}, status=404)
    
    
    def post(self, request):
        serializer = jv_serializers.InventoryRawMaterialsAddSerializer(data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)
        
        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se agregó correctamente.'}, status = 201)
    
    def put(self, request):
        id = request.data.get('id') 
        instance = self.get_object(id)
        serializer = jv_serializers.InventoryRawMaterialsEditSerializer(instance, data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)

        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se editó correctamente.'}, status = 200)
    
    def delete(self, request):
        id = request.data.get('id') 
        request.data.update({'status': False})
        instance = self.get_object(id)
        serializer = jv_serializers.InventoryRawMaterialsCancelSerializer(instance, data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)

        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se editó correctamente.'}, status = 200)

class ProductsMaterialsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
  
    def get_object(self, pk):
        try:
            return jv_models.ProductsMaterialsModel.objects.get(pk = pk)
        except jv_models.ProductsMaterialsModel.DoesNotExist:
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

            products_materials = jv_models.ProductsMaterialsModel.objects.filter(
                Q(id__icontains = search_query) |
                Q(quantity__icontains = search_query) 
            )

            if order == 'desc':
                order_by = f'-{order_by}'

            products_materials = products_materials.order_by(order_by)
            paginator = Paginator(products_materials, show)
            products_materials_page = paginator.page(page_number)

            serialized = jv_serializers.ProductsMaterialsTableSerializer(products_materials_page, many = True)

            return JsonResponse({
                'success': True,
                'data': serialized.data,
                'total_pages': paginator.num_pages,
                'current_page': products_materials_page.number
            })
        elif query == 'statistics':
            count_total = jv_models.ProductsMaterialsModel.objects.filter(
            ).count()
            return JsonResponse({
                'success': True,
                'count_total': count_total,
            })
        return JsonResponse({'success': False, 'msg': 'Consulta no encontrada.'}, status=404)
    
    
    def post(self, request):
        serializer = jv_serializers.ProductsMaterialsAddSerializer(data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)
        
        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se agregó correctamente.'}, status = 201)
    
    def put(self, request):
        id = request.data.get('id') 
        instance = self.get_object(id)
        serializer = jv_serializers.ProductsMaterialsEditSerializer(instance, data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)

        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se editó correctamente.'}, status = 200)

class DetailSalesAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
  
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


    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
  
    def get_object(self, pk):
        try:
            return User.objects.get(pk = pk)
        except User.DoesNotExist:
            raise JsonResponse({'success': False, 'msg': 'El usuario  no existe.'}, status = 404)

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

            user = User.objects.filter(
                Q(id__icontains = search_query) |
                Q(username__icontains = search_query)|
                Q(password__icontains = search_query)|
                Q(first_name__icontains = search_query)|
                Q(last_name__icontains = search_query)
            )

            if order == 'desc':
                order_by = f'-{order_by}'

            user = user.order_by(order_by)
            paginator = Paginator(user, show)
            user_page = paginator.page(page_number)

            serialized = jv_serializers.UsersTableSerializer(user_page, many = True)

            return JsonResponse({
                'success': True,
                'data': serialized.data,
                'total_pages': paginator.num_pages,
                'current_page': user_page.number
            })
        elif query == 'info':
            pass
        return JsonResponse({'success': False, 'msg': 'Consulta no encontrada.'}, status=404)
    
    def post(self, request):
        serializer = jv_serializers.UsersAddSerializer(data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)
        
        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se agregó correctamente.'}, status = 201)
    
    def put(self, request):
        id = request.data.get('id') 
        instance = self.get_object(id)
        serializer = jv_serializers.UsersEditSerializer(instance, data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)

        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se editó correctamente.'}, status = 200)

class SalesFinalizeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_product(self, pk):
        try:
            return jv_models.ProductsModel.objects.get(pk=pk)
        except jv_models.ProductsModel.DoesNotExist:
            raise Http404('El producto no existe.')
        
    def post(self, request):
        with transaction.atomic():
            request.data['total'] = 0
            request.data['users_id'] = request.user.id

            serializer = jv_serializers.SalesFinalizeAddSerializer(data = request.data)
            if not serializer.is_valid():
                return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)
            
            sales_instance = serializer.save()
            sales_id = sales_instance.id  
            
            cart = request.data['cart']
            if not cart:
                transaction.set_rollback(True)
                return JsonResponse({'success': False, 'msg': 'Carrito vació'}, status = 400)
            
            sale_total = 0 
            
            for item in cart:
                try:
                    instance_product = self.get_product(item['id'])
                except Http404 as e:
                    return JsonResponse({'success': False, 'msg': str(e)}, status = 404)
                
                item_obj =  {
                    'price': instance_product.price,
                    'products_id': instance_product.id,
                    'sales_id': sales_id,
                    'quantity': item['quantity']
                }
                
                sale_total += item['quantity'] * instance_product.price

                serializer_details = jv_serializers.DetailSalesAddSerializer(data = item_obj)
                if not serializer_details.is_valid():
                    return JsonResponse({'success': False, 'msg': serializer_details.errors}, status = 400)
                
                serializer_details.save()

            sales_instance.total = sale_total
            sales_instance.save()

            return JsonResponse({'success': True,'sale_id': sales_id, 'msg': 'Se finalizó correctamen.'}, status = 200)