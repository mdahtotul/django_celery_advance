import os

# basic envs
django_secret_key = os.environ.get("SECRET_KEY")
debug = os.environ.get("DEBUG")
allowed_hosts = os.environ.get("ALLOWED_HOSTS")

# celery envs
celery_broker_url = os.environ.get(
    "CELERY_BROKER_URL",
    "redis://redis:6379/0",
)
celery_result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://redis:6379/0")
