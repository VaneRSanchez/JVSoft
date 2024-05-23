from django.urls import path
import api.views as jv_views

urlpatterns = [
    path('auth/sign-in', jv_views.SignInAPIView.as_view(), name='api-sign-in'),
    path('product/categories', jv_views.ProductCategoriesAPIView.as_view(), name='api-product-categories'),
    path('products', jv_views.ProductsAPIView.as_view(), name='api-products'),
    path('products/materials', jv_views.ProductsMaterialsAPIView.as_view(), name='api-products-materials'),
    path('raw/material/categories', jv_views.RawMaterialCategoriesAPIView.as_view(), name='api-raw-material-categories'),
    path('raw/materials', jv_views.RawMaterialsAPIView.as_view(), name='api-raw-materials'),
    path('inventory/raw/materials', jv_views.InventoryRawMaterialsAPIView.as_view(), name='api-inventory-raw-materials'),
    path('units', jv_views.UnitsAPIView.as_view(), name='api-units'),
    path('movement/types', jv_views.MovementTypesAPIView.as_view(), name='api-movement-types'),
    path('sales', jv_views.SalesAPIView.as_view(), name='api-sales'),
    path('detail/sales', jv_views.SalesAPIView.as_view(), name='api-detail-sales'),
    path('sale/finalize', jv_views.SalesFinalizeAPIView.as_view(), name='sale-finalize'),
]
