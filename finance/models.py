from django.db import models
from accounts.models import UserProfile

class Account(models.Model):
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='accounts',
        verbose_name='Usuário'
    )

    name = models.CharField(
        max_length=100,
        verbose_name='Nome da Conta'
    )

    type = models.CharField(
        max_length=20,
        choices=[
        ('CHECKING', 'Conta Corrente'),
        ('SAVINGS', 'Conta Poupança'),
        ('INVESTMENT', 'Investimento')],
        default='CHECKING',
        verbose_name='Tipo de Conta'
    )
    balance = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        default=0.00, 
        verbose_name='Saldo atual'
    )
    bank_name = models.CharField(
        max_length=100, 
        blank=True,
        null=True, 
        verbose_name='Banco'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Conta Ativa'
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
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'

    def __str__(self):
        return f'{self.name} - {self.get_type_display()}'
    
class Card(models.Model):
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='cards',
        verbose_name='Conta'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Nome do Cartão'
    )
    credit_limit = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
        verbose_name='Limite de Crédito'
    )
    used_limit = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
        verbose_name='Limite Utilizado'
    )
    closing_day = models.IntegerField(
        choices=[(i, i) for i in range(1, 32)],
        verbose_name='Dia de Fechamento'
    )
    due_day = models.IntegerField(
        choices=[(i, i) for i in range(1, 32)],
        verbose_name='Dia de Vencimento'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Cartão Ativo'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )

    class Meta:
        verbose_name = 'Cartão'
        verbose_name_plural = 'Cartões'
    
    def __str__(self):  
        return f'{self.name} - Limite: {self.credit_limit} - Utilizado: {self.used_limit}'

    