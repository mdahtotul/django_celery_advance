from celery import Celery

app = Celery("django_celery_2")
app.config_from_object("celery_config", namespace="CELERY")
app.conf.imports = ("playground.tasks",)
app.autodiscover_tasks()
