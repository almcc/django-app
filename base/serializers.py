from django_celery_beat.models import PeriodicTask, IntervalSchedule, CrontabSchedule, \
    PeriodicTasks, SolarSchedule
from rest_framework import serializers

from base.models import Profile


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
