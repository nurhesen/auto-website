#!/bin/bash

HOST=db
PORT=3306

# Loop until the connection is successful
while ! telnet $HOST $PORT >/dev/null 2>&1; do
    echo "Waiting for connection to $HOST:$PORT..."
    sleep 1  # Adjust the interval between connection attempts as needed
done

echo "Connection to $HOST:$PORT is active!"

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata db_dump.json
python manage.py collectstatic --noinput


gunicorn --bind 0.0.0.0:8000 auto.wsgi

# gunicorn auto.wsgi:application --bind 0.0.0.0:8000