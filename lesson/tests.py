from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from lesson.models import Lesson, Course
from users.models import User

class LessonTestCase(APITestCase):
    def create_user(self):
        """Создание пользователя"""
        self.user = User.objects.create(
            email='test@test.com',
            is_staff=False,
            is_active=True,
        )
        self.user.set_password('1234')
        self.user.save()

    def setUp(self) -> None:
        """Подготовка данных"""
        self.create_user()

        self.course = Course.objects.create(
            title='course test',
            description='list test description',
            owner=self.user
        )

        self.lesson = Lesson.objects.create(
            title='list test',
            description='list test description',
            owner=self.user
        )

    def test_list_lesson(self):
        """Тестирование вывода списка уроков"""

        response = self.client.get(
            reverse('lesson:lesson_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': 4, 'course': None, 'title': 'list test', 'description': 'list test description', 'preview': None,
                 'url_video': None, 'owner': 3}]}
        )

    def test_create_lesson(self):
        """Тестирование создания уроков"""
        self.client.force_authenticate(self.user)

        data = {
            'title': 'test',
            'description': 'test description',
            'course': self.course.title
        }

        response = self.client.post(
            reverse('lesson:lesson_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Lesson.objects.count(),
            2
        )

    def test_update_lesson(self):
        """Тестирование обновления"""
        self.client.force_authenticate(self.user)
        data = {
            'title': 'test lesson updated',
        }

        response = self.client.patch(
            reverse("lesson:lesson_update", kwargs={'pk': self.lesson.id}),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        # Check updated name

        self.assertEqual(
            Lesson.objects.get(pk=self.lesson.id).title,
            'test lesson updated'
        )

    def test_delete_lesson(self):
        """Тестирование удаления урока"""
        self.client.force_authenticate(self.user)
        response = self.client.delete(
            reverse("lesson:lesson_delete", kwargs={'pk': self.lesson.id})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        # Check that no lesson exists in Database
        self.assertFalse(
            Lesson.objects.exists()
        )