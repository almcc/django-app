from django_celery_beat.models import (CrontabSchedule, IntervalSchedule,
                                       PeriodicTask, SolarSchedule)
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from base.serializers import (CrontabScheduleSerializer,
                              IntervalScheduleSerializer,
                              PeriodicTaskSerializer, SolarScheduleSerializer)


class PeriodicTaskViewSet(viewsets.ModelViewSet):
    queryset = PeriodicTask.objects.all()
    serializer_class = PeriodicTaskSerializer
    permission_classes = (IsAdminUser,)


class IntervalScheduleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = IntervalSchedule.objects.all()
    serializer_class = IntervalScheduleSerializer


class CrontabScheduleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CrontabSchedule.objects.all()
    serializer_class = CrontabScheduleSerializer


class SolarScheduleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SolarSchedule.objects.all()
    serializer_class = SolarScheduleSerializer
