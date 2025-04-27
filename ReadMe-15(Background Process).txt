# 15-1 [Background Process] in Background Process we make a "Queue" (صف) and all task "FIFO" entered in to queue. "app" send task to "queue" and "queue" send tasks to empty "worker"
# if we don't have worker empty and Queue became full, jobs are lost! /// "Broker" (واسط) has move task from "App", "Queue", "worker" /// Broker module in django: redis , rabbitmq
# redis is Broker -> https://github.com/redis/redis
# python "Celery" can get communication between "Redis" (Broker) & Worker  -> https://docs.celeryq.dev/en/stable/getting-started/introduction.html

# 15-2 [Run redis in server and docker compose]













