from django.shortcuts import render
from base.tasks import example
import logging

logger = logging.getLogger('base.views')

def index(request):
    try:
        example.delay()  # trigger a background task
    except example.OperationalError as exc:
        logger.exception('Sending task raised: %r', exc)
    return render(request, 'base/index.html', {})
