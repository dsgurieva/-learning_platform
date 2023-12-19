from rest_framework import viewsets, generics
from lesson.models import Course, Lesson
from lesson.paginators import LessonPaginator, CoursePaginator
from lesson.permissions import IsStaff, IsOwner
from lesson.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from rest_framework.permissions import IsAuthenticated #, AllowAny


class CourseViewSet(viewsets.ModelViewSet):
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


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated | IsStaff]
    #permission_classes = [AllowAny]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsStaff]
    pagination_class = LessonPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsStaff]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsStaff]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsStaff]


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer

    def perform_create(self, serializer):
        new_subscribe = serializer.save()
        new_subscribe.user = self.request.user
        new_subscribe.save()


class SubscriptionListAPIView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner, IsStaff]


class SubscriptionDeleteAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner, IsStaff]