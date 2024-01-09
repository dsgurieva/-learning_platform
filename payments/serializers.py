from rest_framework import serializers
from payments.models import Payments
from payments.services.payment import create_payment


class PaymentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'

    def create(self, validated_data):
        payment = Payments(
            payment_amount=validated_data["payment_amount"],
            payment_method=validated_data["payment_method"],
            payment_id=create_payment(validated_data['payment_amount']),
        )
        payment.save()
        return payment