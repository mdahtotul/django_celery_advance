### Python commands

```
pip freeze > requirements.txt
```

### Docker commands

```
docker compose up -d --build
```

### Celery commands

```
For macos/linux: celery -A <app_name> worker -l info
For windows: celery -A <app_name> worker --pool=solo -l info
```

### Lesson:

4-> 4. Creating a new standalone Celery Worker
