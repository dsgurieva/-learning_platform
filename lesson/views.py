from rest_framework import viewsets, generics
from lesson.models import Course, Lesson
from lesson.paginators import LessonPaginator, CoursePaginator
from lesson.permissions import IsStaff, IsOwner
from lesson.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from rest_framework.permissions import IsAuthenticated #, AllowAny\
from lesson.tasks import _send_email


class CourseViewSet(viewsets.ModelViewSet):
    """Viewset for course"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CoursePaginator

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [IsOwner | IsStaff]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated | IsStaff]
        elif self.action == 'destroy':
            permission_classes = [IsOwner | IsStaff]
        elif self.action == 'update':
            permission_classes = [IsOwner | IsStaff]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        updated_course = serializer.save()
        _send_email.delay(updated_course.pk)


class LessonCreateAPIView(generics.CreateAPIView):
    """Lesson create API view"""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated | IsStaff]
    #permission_classes = [AllowAny]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """Lesson list API view"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsStaff]
    pagination_class = LessonPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Lesson retrieve API view"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsStaff]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Lesson update API view"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsStaff]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Lesson delete API view"""
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsStaff]


class SubscriptionCreateAPIView(generics.CreateAPIView):
    """Subscription create API view"""
    serializer_class = SubscriptionSerializer

    def perform_create(self, serializer):
        new_subscribe = serializer.save()
        new_subscribe.user = self.request.user
        new_subscribe.save()


class SubscriptionListAPIView(generics.ListAPIView):
    """Subscription list API view"""
    serializer_class = SubscriptionSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner, IsStaff]


class SubscriptionDeleteAPIView(generics.DestroyAPIView):
    """Subscription delete API view"""
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner, IsStaff]