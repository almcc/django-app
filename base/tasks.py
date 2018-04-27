from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger('tasks.base')


@shared_task(bind=True)
def example(self):
    logger.debug('example')
