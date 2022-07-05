
from django.urls import path 
from .views import cart , cart_add , cart_remove



app_name = 'cart'

# urlpatterns = [
    
#     path('', cart , name='cart'),

# ]


urlpatterns = [
    path('my/cart/detail/', cart, name='cart'),
    path('cart/add/<int:product_id>/', cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', cart_remove,name='cart_remove'),
]