from django.db import models


class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self
