from payments.apps import PaymentsConfig
from payments.views import PaymentsListAPIView
from django.urls import path


app_name = PaymentsConfig.name


urlpatterns = [
    path('', PaymentsListAPIView.as_view(), name='payments_list'),
]