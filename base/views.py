from django.shortcuts import render
from base.tasks import example


def index(request):
    example.delay()  # trigger a background task
    return render(request, 'base/index.html', {})
