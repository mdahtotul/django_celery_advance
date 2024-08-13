### Python commands

```
python manage.py shell
python manage.py runserver
pip freeze > requirements.txt
```

### Docker commands

```
docker compose up -d --build
docker compose down
docker exec -it <app_name> /bin/sh
```

### Celery commands

```
For macos/linux: celery -A <app_name> worker -l info
For windows: celery -A <app_name> worker --pool=solo -l info
```

### Lesson:

Done: 4-> 13. Passing arguments and returning results from Celery tasks

### Celery Code

```
# for grouping and chaining tasks using celery
from celery import group, chain
from playground.tasks import tp1, tp2, tp3, tp4, tp5, task1
task_group = group(tp1.s(), tp2.s(), tp3.s(), tp4.s())
task_group.apply_async()

task_chain = chain(tp1.s(), tp2.s(), tp3.s())
task_chain.apply_async()
```
