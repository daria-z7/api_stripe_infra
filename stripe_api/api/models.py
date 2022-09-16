from django.db import models


CHOICES = (
    ("eur", "eur"),
    ("usd", "usd"),
)


class Item(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=200,
    )
    description = models.TextField(
        verbose_name='Description',
    )
    price = models.IntegerField(
        verbose_name='Price',
    )
    currency = models.CharField(
        verbose_name="Currency",
        max_length=10,
        choices=CHOICES,
    )

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name
