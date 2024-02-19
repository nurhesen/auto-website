# With Docker easy peasy

```

docker-compose build
docker-compose up

```


There will be an admin account created automatically

Go to http://127.0.0.1:8000/admin/
Type theese and enter

```
username: admin
password: admin

```


# If you don't want to use Docker then



# Clone the project

```

git clone https://github.com/nurhesen/auto-website.git
cd auto-website

```

# Backend

Create virtualenvironment at core folder

```

virtualenv venv
pip install -r requirements.txt

```

Run Backend on http://127.0.0.1:8000

```

python manage.py runserver

```
Now you can see the project at http://127.0.0.1:8000

If you want to run frontend separately then

# Frontend

Go to frontend folder

```

cd frontend

```

install all packages

```

yarn install

```

Run frontend on http://localhost:3000

```

yarn start

```
Now you can go to http://localhost:3000 and view the project
