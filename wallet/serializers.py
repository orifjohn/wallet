from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Wallet, WalletTransaction


# class UserSerializer(serializers.ModelSerializer):
#     # class Meta:
#     #     model = User
#     #     fields = "__all__"
#     id = serializers.IntegerField()
#     username = serializers.CharField()
#     is_staff = serializers.BooleanField()
#     is_active = serializers.BooleanField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff', 'is_active',)


# class WalletSerializer(serializers.Serializer):
#     wallet_id = serializers.CharField(max_length=16)
#     balance = serializers.IntegerField()
#     user = UserSerializer()

class WalletSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Wallet
        fields = ('id', 'wallet_id', 'balance', 'user',)


class CreateTransactionSerializer(serializers.Serializer):
    from_wallet_id = serializers.CharField(max_length=16)
    to_wallet_id = serializers.CharField(max_length=16)
    amount = serializers.IntegerField()


class WalletTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletTransaction
        fields = '__all__'
