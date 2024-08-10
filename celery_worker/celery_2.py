from celery import Celery

app = Celery("django_celery_2")
app.config_from_object("celery_config", namespace="CELERY")


@app.task
def check_app_2():
    return
