import os

from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import stripe
from dotenv import load_dotenv

from api.models import Item

load_dotenv('../infra/.env')


stripe.api_key = os.getenv('STRIPE_SK')
url_base = os.getenv('URL_PATH')


@api_view(['GET'])
def create_payment(request, item_id):
    """Функция для проведения платежа."""
    item = get_object_or_404(Item, id=item_id)
    product = stripe.Product.create(name=item.name)
    price = stripe.Price.create(
        unit_amount=item.price * 100,
        currency=item.currency,
        product=product,
    )
    items = [url_base, "item", str(item_id)]
    url = "/".join(
        [
            (u.strip("/") if index + 1 < len(items) else u.lstrip("/")) for index, u in enumerate(items)
        ]
    )
    response = stripe.checkout.Session.create(
        success_url=url,
        cancel_url=url,
        line_items=[
            {
                "price": price,
                "quantity": 1,
            },
        ],
        mode="payment",
        payment_method_types=["card",]
    )
    return Response(response["id"])


@api_view(['GET'])
def get_item(request, item_id):
    """Функция для отображения информации о товаре."""
    item = get_object_or_404(Item, id=item_id)
    context = {
        "item": item,
        "stripe_pk_key": os.getenv('STRIPE_PK')
    }
    return render(request, 'api/item_description.html', context)
