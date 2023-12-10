from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from lesson.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field="title", queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, source='lesson', read_only=True)
    lessons_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, instance):
        return instance.lesson.count()






