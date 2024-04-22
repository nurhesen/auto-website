#!/bin/bash

HOST=db_auto_website
PORT=3306

# Loop until the database connection is successful
while ! telnet $HOST $PORT >/dev/null 2>&1; do
    echo "Waiting for connection to $HOST:$PORT..."
    sleep 1  # Adjust the interval between connection attempts as needed
done

echo "Connection to Database $HOST:$PORT is active!"

python manage.py makemigrations
# python manage.py migrate
# python manage.py loaddata db_dump.json
# cp -r /temp_media/media /usr/src/app
python manage.py migrate
python manage.py collectstatic --noinput


gunicorn --bind 0.0.0.0:8000 auto.wsgi
