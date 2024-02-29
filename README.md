# Deploy with one click at my AWS instance:

[nurhesen.click/auto-website-deploy](https://www.nurhesen.click/deploy)

P.S: Instance will only be active for 10 minutes after it is deployed


# For development on local pc:

Clone the repository:

```
git clone https://github.com/nurhesen/auto-website.git

```

Enter the folder:
```
cd auto-website

```
Configure .env file for your preferences.

Build and run docker-compose:

```
docker-compose build
docker-compose up

```



Frontend is hosted at [localhost:3000](http://localhost:3000/)
Backend is hosted at [localhost:8000](http://localhost:8000/)

Go to [localhost:8000/admin/](http://localhost:8000/admin/)
There will be an admin account created automatically from database dump
Type theese and enter

```
username: admin
password: admin

```


# For deployment (Deployment scripts are for Ubuntu 20.04):

Clone the repository:

```
git clone https://github.com/nurhesen/auto-website.git

```

Enter the folder:
```
cd auto-website

```

Edit the .env file for your needs and run deploy.sh script:
```
nano .env
source deploy.sh yourdomain.com

```

