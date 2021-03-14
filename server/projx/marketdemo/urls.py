
from django.urls import path, include
# from .views import product_list, product_detail
# from .views import ProductAPIView, ProductDetails, ProductDetail
from .views import ProductList
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('products', ProductList, basename='products')

urlpatterns = [
    path('', include(router.urls)),
    # path('products/', product_list),
    # path('products/', ProductAPIView.as_view()),
    # path('product/<int:id>', ProductDetail.as_view()),
    # path('product/<int:pk>', product_detail),
    # path('product/<int:id>', ProductDetails.as_view()),

]
