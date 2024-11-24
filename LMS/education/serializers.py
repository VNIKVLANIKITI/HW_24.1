from rest_framework import serializers
from education.models import lesson, course

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = lesson
        #fields = '__all__'
        fields = ('name', 'description',)


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = course
        #fields = '__all__'
        fields = ('name', 'description','lessons',)