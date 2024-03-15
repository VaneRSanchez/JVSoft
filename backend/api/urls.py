from django.urls import path
import api.views as jv_views

urlpatterns = [
    path('auth/sign-in', jv_views.SignInAPIView.as_view(), name='api-sign-in'),
    path('product/categories', jv_views.ProductCategoriesAPIView.as_view(), name='api-product-categories')
]
