from django.urls import path

from api.views import create_payment, get_item


app_name = 'api'

urlpatterns = [
    path('buy/<int:item_id>/', create_payment, name='payment'),
    path('item/<int:item_id>/', get_item, name='item_page'),
]
