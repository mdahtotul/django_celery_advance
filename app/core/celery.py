import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("django_celery")
app.config_from_object("django.conf:settings", namespace="CELERY")


@app.task
def add_numbers():
    return


app.autodiscover_tasks()
