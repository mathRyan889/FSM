from django.db import models
from accounts.models import UserProfile
from transactions.models import Category

class Budget(models.Model):
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.PROTECT,
        related_name='budgets',
        verbose_name='Usuário'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='budgets',
        verbose_name='Categoria'
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Valor de Meta'
    )
    month = models.IntegerField(
        verbose_name='Mês',
        choices=[(i, i) for i in range(1, 13)]
    )
    year = models.IntegerField(
        verbose_name='Ano',
        choices=[(i, i) for i in range(2020, 2031)]
    )
    alert_sent = models.BooleanField(
        default=False,
        verbose_name='Alerta Enviado'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )

    class Meta:
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'

    def __str__(self):
        return f'Orçamento de {self.category.name} para {self.month}/{self.year}'
