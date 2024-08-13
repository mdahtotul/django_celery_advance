import os
import time
from celery import Celery
from kombu import Queue, Exchange

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("django_celery")
app.config_from_object("django.conf:settings", namespace="CELERY")

########### RabbitMQ ################
app.conf.task_queues = [
    Queue(
        "tasks",
        Exchange("tasks"),
        routing_key="tasks",
        queue_arguments={"x-max-priority": 10},
    )
]
app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1


@app.task(queue="tasks")
def t1(a, b, message=None):
    result = a + b
    if message:
        result = f"{message}: {result}"
    return result


@app.task(queue="tasks")
def t2():
    time.sleep(3)
    return


@app.task(queue="tasks")
def t3():
    time.sleep(3)
    return


########### RabbitMQ ################


########### Redis ################
# task routing
# app.conf.task_routes = {
#     # "app.tasks.*": {"queue": "celery"},
#     "playground.tasks.task1": {"queue": "queue1"},
#     "playground.tasks.task2": {"queue": "queue2"},
# }


# app.conf.broker_transport_options = {
#     "priority_steps": list(range(10)),
#     "sep": ":",
#     "queue_order_strategy": "priority",
# }
########### Redis ################
app.autodiscover_tasks()


def test():
    result = t1.apply_async(args=[5, 10], kwargs={"message": "The sum is"})

    # Check if the task has been completed
    if result.ready():
        print("Task completed")
    else:
        print("Task is still running")

    # Check if the task completed successfully
    if result.successful():
        print("Task completed successfully")
    else:
        print("Task encountered an error")

    # Get the result
    try:
        task_result = result.get()
        print(f"Task result: {task_result}")
    except Exception as e:
        print("An exception occurred", str(e))

    # Get the exception (if any) that occurred during task execution
    exception = result.get(propagate=False)
    if exception:
        print("An exception occurred", str(exception))
