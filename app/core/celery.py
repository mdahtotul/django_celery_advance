import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("django_celery")
app.config_from_object("django.conf:settings", namespace="CELERY")

# task routing
# app.conf.task_routes = {
#     # "app.tasks.*": {"queue": "celery"},
#     "playground.tasks.task1": {"queue": "queue1"},
#     "playground.tasks.task2": {"queue": "queue2"},
# }


app.conf.broker_transport_options = {
    "priority_steps": list(range(10)),
    "sep": ":",
    "queue_order_strategy": "priority",
}

app.autodiscover_tasks()
