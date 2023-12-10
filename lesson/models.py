from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='avatar/', verbose_name='превью', null=True, blank=True)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='avatar/', verbose_name='превью', null=True, blank=True)
    description = models.TextField(verbose_name='описание')
    url_video = models.URLField(max_length=200, verbose_name='ссылка на видео', null=True, blank=True)

    course = models.ForeignKey(Course, verbose_name="курс", null=True, blank=True, on_delete=models.CASCADE,
                               related_name="lesson")

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
