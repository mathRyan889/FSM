from django.db import models
from accounts.models import UserProfile
from finance.models import Account, Card


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Nome da Categoria'
    )
    icon = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Ícone (opcional)'
    )
    color = models.CharField(
        max_length=7,
        blank=True,
        null=True,
        verbose_name='Cor (opcional, formato HEX)'
    )
    type = models.CharField(
        max_length=20,
        choices=[
            ('INCOME', 'Receita'),
            ('EXPENSE', 'Despesa'),
            ('BOTH', 'Ambos')
        ],
        default='EXPENSE',
        verbose_name='Tipo de Categoria'
    )
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        null=True,
        related_name='categories',
        verbose_name='Usuário'
    )


    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.name
    
class Transaction(models.Model):
    account = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name='transactions',
        verbose_name='Conta'
    )
    card = models.ForeignKey(
        Card,
        on_delete=models.PROTECT,
        related_name='transactions',
        verbose_name='Cartão',
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='transactions',
        verbose_name='Categoria'
    )
    type = models.CharField(
        max_length=20,
        choices=[
            ('INCOME', 'Receita'),
            ('EXPENSE', 'Despesa')
        ]
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Valor'
    )
    description = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Descrição'
    )
    date = models.DateField(
        verbose_name='Data da Transação'
    )
    is_recurring = models.BooleanField(
        default=False,
        verbose_name='Transação Recorrente'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em'
    )

    class Meta:
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'
    
    def __str__(self):
        return f'{self.get_type_display()} - {self.amount} em {self.date}'




