from django.db import models
from config import settings
from lesson.models import Course, Lesson


class Payments(models.Model):
    CASH = 'cash'
    TRANSFER_TO_ACCOUNT = 'transfer to account'

    PAYMENT_METHOD = (
        (CASH, 'Наличными'),
        (TRANSFER_TO_ACCOUNT, 'Перевод на счет')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='пользователь', null=True, blank=True)
    payment_date = models.DateField(auto_now_add=True, verbose_name='дата оплаты')
    payment_amount = models.IntegerField(verbose_name='сумма оплаты')
    payment_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', null=True, blank=True)
    payment_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок', null=True, blank=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD, verbose_name='способ оплаты')

    payment_id = models.CharField(max_length=100, verbose_name="payment_id", null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.payment_course} or {self.payment_lesson}"

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'



