from celery import shared_task


@shared_task
def delayed_tasks():
    return True
