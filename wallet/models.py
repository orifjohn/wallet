from django.db import models
from django.db.models import constraints


class Wallet(models.Model):
    wallet_id = models.CharField(max_length=16, unique=True, db_index=True)
    balance = models.IntegerField(default=10000)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.wallet_id} | {self.balance}"

    class Meta:
        constraints = [
            constraints.CheckConstraint(check=models.Q(balance__gte=0), name='balance_gte_0')
        ]


class WalletTransaction(models.Model):
    from_wallet = models.ForeignKey("Wallet", on_delete=models.SET_NULL, null=True, related_name="from_wallet")
    to_wallet = models.ForeignKey("Wallet", on_delete=models.SET_NULL, null=True, related_name="to_wallet")
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.from_wallet.wallet_id} -> {self.to_wallet.wallet_id}"
