from rest_framework import views, response, validators
from rest_framework.decorators import api_view
from .models import Wallet, WalletTransaction
from .serializers import WalletSerializer, CreateTransactionSerializer, WalletTransactionSerializer


# @api_view(['GET', 'POST'])
# def index_view(request):
#     pass

# class WalletListView(views.APIView):
#     def get(self, request):
#         queryset = Wallet.objects.all()
#         serializer = WalletSerializer(queryset, many=True)
#         return response.Response({'wallet list': serializer.data})

class WalletView(views.APIView):
    def get(self, request, wallet_id):
        try:
            instance = Wallet.objects.get(wallet_id=wallet_id)
            serializer = WalletSerializer(instance)
            return response.Response(serializer.data)
        except Wallet.DoesNotExist:
            raise validators.ValidationError({'message': 'user not found'})


class TransactionView(views.APIView):
    def post(self, request):
        serializer = CreateTransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(vars(serializer))
        from_wallet = Wallet.objects.get(wallet_id=serializer.data.get("from_wallet_id"))
        to_wallet = Wallet.objects.get(wallet_id=serializer.data.get("to_wallet_id"))

        from_wallet.balance -= serializer.data.get("amount")
        to_wallet.balance += serializer.data.get("amount")

        try:
            from_wallet.save()
            to_wallet.save()
        except Exception as e:
            raise validators.ValidationError({'message': "min value 0"})

        wt_transaction = WalletTransaction.objects.create(
            from_wallet=from_wallet,
            to_wallet=to_wallet,
            amount=serializer.data.get("amount"))

        transaction_serializer = WalletTransactionSerializer(wt_transaction)
        return response.Response(transaction_serializer.data)

    # def post(self, request):
    #     from_wallet_id = WalletTransaction.objects.first().from_wallet
    #     to_wallet_id = WalletTransaction.objects.first().from_wallet
    #     amount = WalletTransaction.objects.first().amount
    #     from_wallet_id -= amount
    #     to_wallet_id += amount
