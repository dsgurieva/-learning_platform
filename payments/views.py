import stripe
from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from payments.models import Payments
from payments.serializers import PaymentsSerializer


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ('payment_date',)
    filter_fields = ('payment_course', 'payment_lesson', 'payment_method',)

    def create_payment(self):
        stripe.api_key = "sk_test_51OQSKmA019y72R72lU8NPNVqX6oUooHlfeawh7oxUxbBlmY6sRZX40mQ8mKSY1OdLYuXyKTGCncNg9Ao08l3g8o4003Tib0dzI"
        pay = stripe.PaymentIntent.create(
            amount=self.queryset.payment_amount,
            currency="usd",
            automatic_payment_methods={"enabled": True},
        )
        pay.save()

    def view_payment(self):
        stripe.api_key = "sk_test_51OQSKmA019y72R72lU8NPNVqX6oUooHlfeawh7oxUxbBlmY6sRZX40mQ8mKSY1OdLYuXyKTGCncNg9Ao08l3g8o4003Tib0dzI"
        view_pay = stripe.PaymentIntent.retrieve(
            Payments.objects.id
        )
        view_pay.save()