from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Transaction


@receiver(post_save, sender=Transaction)
# Atualiza o saldo da conta associada à transação após salvar uma nova transação
# ou atualizar uma existente
def update_balance_on_save(sender, instance, created, **kwargs):

    account = instance.account

    if created:
        # Nova transação criada
        if instance.type == 'INCOME':
            account.balance += instance.amount  # Se for receita, adiciona ao saldo
        else:
            account.balance -= instance.amount  # Se for despesa, subtrai do saldo

        account.save()


@receiver(post_delete, sender=Transaction)
# Atualiza o saldo da conta associada à transação após excluir uma transação
def update_balance_on_delete(sender, instance, **kwargs):

    account = instance.account

    if instance.type == 'INCOME':
        account.balance -= instance.amount  # Se for receita, subtrai do saldo
    else:
        account.balance += instance.amount  # Se for despesa, adiciona ao saldo

    account.save()
