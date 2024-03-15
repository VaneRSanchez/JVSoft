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

    def post(self, request):
        serializer = jv_serializers.ProductCategoriesAddSerializer(data = request.data)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status = 400)
        
        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se agregó correctamente.'}, status = 201)
    
    def put(self, request):
        id = request.query_params.get('id') if str(id).isnumeric() else 0
        instance = self.get_object(id)
        serializer = jv_serializers.ProductCategoriesEditSerializer(instance, data=request.query_params)
        if not serializer.is_valid():
            return JsonResponse({'success': False, 'msg': serializer.errors}, status=400)

        serializer.save()
        return JsonResponse({'success': True, 'msg': 'Se editó correctamente.'}, status=200)