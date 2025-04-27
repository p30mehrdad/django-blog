# 15-1 [Background Process] in Background Process we make a "Queue" (صف) and all task "FIFO" entered in to queue. "app" send task to "queue" and "queue" send tasks to empty "worker"
# if we don't have worker empty and Queue became full, jobs are lost! /// "Broker" (واسط) has move task from "App", "Queue", "worker" /// Broker (transport) module in django: redis , rabbitmq
# redis is Broker -> https://github.com/redis/redis
# python "Celery" can get communication between "Redis" (Broker) & Worker  -> https://docs.celeryq.dev/en/stable/getting-started/introduction.html


# 15-2 [Run redis in docker compose] port 6379:6379 is default for redis -> https://hub.docker.com/_/redis & https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/docker/
docker-compose exec backend sh
pip install redis
exit
docker-compose down
# make edit docker-compose.yml / add new services: (upper of backend)

redis:
    container_name: redis
    image: redis
    ports:
      - "6379:6379"
    command: redis-server --save 60 1 --loglevel warning

# save docker compose and run again
docker-compose up -d
# check redis: (cli -> command line)
docker-compose exec -it redis sh
redis-cli
ping
# return "PONG" -> it means redis is okay and our Broker is online now


# 15-3 [Run Celery] make new file in: "proj/proj/celery.py" (proj=core) // beside of settings.py -> https://docs.celeryq.dev/en/latest/django/first-steps-with-django.html
docker-compose exec backend sh
pip install celery
# update "proj/proj/__init__.py" -> from .celery import app as celery_app
# add to settings : CELERY_BROKER_URL -> set address of redis
# for run celery:
docker-compose exec backend sh
# celery -A proj worker -l INFO
celery -A core worker -l INFO
# return : Connected to redis://redis:6379/1


# 15-4 [add worker (celery) to docker compose] add depends_on: to backend in docker-compose.yml
docker-compose down
# add restart: always to redis in docker-compose
# add new services: to docker-compose ->  worker:
docker-compose up -d

# 15-5 [make task] make urls in "accounts/urls.py" -> path("send-email/", views.send_email, name="send-email"), and make "views" send_email()
# need delete "path("api/v1/", include("accounts.api.v1.urls"))," in urls.py
# make "tasks.py" in accounts folder and use "from celery import shared_task"
docker-compose down
docker-compose up
# go to http://127.0.0.1:8000/accounts/send-email/ , and after 3 sec in terminal print text / print('done sending email')












