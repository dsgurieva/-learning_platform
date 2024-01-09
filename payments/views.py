import stripe
from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from lesson.models import Course
from payments.models import Payments
from payments.serializers import PaymentsSerializer


class PaymentListAPIView(generics.ListAPIView):
    """Просмотр платежей"""
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # Изменение последовательности
    ordering_fields = ('date_of_payment',)
    # фильтрация по полям
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method',)


class PaymentCreateAPIView(generics.CreateAPIView):
    """Создание платежа"""
    serializer_class = PaymentsSerializer

    def perform_create(self, serializer):
        """Сохраняет пользователя и курс"""
        new_payment = serializer.save()
        new_payment.user = self.request.user
        new_payment.course = Course.objects.get(pk=self.kwargs.get('pk'))
        new_payment.save()


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentsSerializer

    def get_object(self):
        object = Payments.objects.get(
            user=self.request.user,
            paid_course=Course.objects.get(pk=self.kwargs.get('pk'))
        )
        return object