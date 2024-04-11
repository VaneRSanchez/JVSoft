from django.urls import path
import api.views as jv_views

urlpatterns = [
    path('auth/sign-in', jv_views.SignInAPIView.as_view(), name='api-sign-in'),
    path('product/categories', jv_views.ProductCategoriesAPIView.as_view(), name='api-product-categories'),
    path('products', jv_views.ProductsAPIView.as_view(), name='api-products'),
    path('products/materia', jv_views.ProductsMateriaAPIView.as_view(), name='api-products-materia'),
    path('raw/material/categories', jv_views.RawMaterialCategoriesAPIView.as_view(), name='api-raw-material-categories'),
    path('raw/materials', jv_views.RawMaterialsAPIView.as_view(), name='api-raw-materials'),
    path('inventary/raw/materials', jv_views.InventaryRawMaterialsAPIView.as_view(), name='api-inventary-raw-materials'),
    path('units', jv_views.UnitsAPIView.as_view(), name='api-units'),
    path('movement/types', jv_views.MovementTypesAPIView.as_view(), name='api-movement-types'),
    path('sales', jv_views.SalesAPIView.as_view(), name='api-sales'),
    path('detail/sales', jv_views.SalesAPIView.as_view(), name='api-detail-sales'),
    
]
