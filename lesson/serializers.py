from rest_framework import serializers
from lesson.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("title", "description")


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ("title", "description")