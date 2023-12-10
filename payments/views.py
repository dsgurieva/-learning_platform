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