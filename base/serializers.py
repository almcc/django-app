from django_celery_beat.models import (CrontabSchedule, IntervalSchedule,
                                       PeriodicTask, SolarSchedule)
from rest_framework import serializers


class PeriodicTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PeriodicTask
        fields = '__all__'


class IntervalScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IntervalSchedule
        fields = '__all__'


class CrontabScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CrontabSchedule
        fields = '__all__'


class SolarScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SolarSchedule
        fields = '__all__'
