from django.urls import path
from .views import index ,  product_detail




app_name = 'products'




urlpatterns = [
    path('',index,name='index'),
    path('<slug:slug>/', index,name='index'),
    path('<str:cat_slug>/<str:product_slug>/', product_detail , name='product_detail'),
    # path(''),
]