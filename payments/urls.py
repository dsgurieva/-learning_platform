from payments.apps import PaymentsConfig
from payments.views import PaymentListAPIView, PaymentCreateAPIView, PaymentRetrieveAPIView
from django.urls import path


app_name = PaymentsConfig.name


urlpatterns = [
    path('', PaymentListAPIView.as_view(), name='payments_list'),
    path('create/courses/<int:pk>/', PaymentCreateAPIView.as_view(), name='payment-create'),
    path('<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment-status'),
]