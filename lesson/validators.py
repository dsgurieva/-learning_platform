from rest_framework.validators import ValidationError


class UrlVideoValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        url_video = value.get('url_video')
        if url_video is not None and 'www.youtube' not in url_video:
            raise ValidationError('Вы можете прикреплять материалы только с YouTube')

