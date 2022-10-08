docker network create my_network
docker network ls  
cd dba
docker build -t my_dba .
docker run --name mydba --network my_network -p 8080:81 -d my_dba
cd ..
cd db
docker build -t my_db .
docker run --name mydb --network my_network   -itd -p5432:5432 my_db
cd ..
docker build -t my_django . 
docker run -it -p8000:8000 -v "$(pwd)/app:/app" my_django /bin/bash
django-admin startproject app
cd app
django-admin startproject app
cd ..
python app/manage.py runserver 0.0.0.0:8000
http://localhost:8000/
http://localhost:8000/admin
python /app/app/manage.py migrate
python /app/app/manage.py createsuperuser
press enter
enter mona@mona.com
enter pass
enter y
python /app/app/manage.py runserver 0.0.0.0:8000
go to browser enter:http://localhost:8000/admin/login/?next=/admin/
find the django data base connect details and enter the details in settings.py (under app/app)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'web',
        'USER': 'root',
        'PASSWORD': 'pass',
        'HOST': 'mydb',
        'PORT': 5432,
    }
}

python /app/app/manage.py migrate
add module in requirements.txt psycopg2
exit
docker build -t my_django .   
docker run -it -p8000:8000 -v "$(pwd)/app:/app" my_django /bin/bash
python /app/app/manage.py migrate
exit
docker run -it -p8000:8000 --network my_network -v "$(pwd)/app:/app" my_django /bin/bash
python /app/app/manage.py migrate
python /app/app/manage.py runserver 0.0.0.0:8000
ctrl+c
python /app/app/manage.py createsuperuser
press enter
enter mona@mona.com
enter pass
enter y
python /app/app/manage.py runserver 0.0.0.0:8000
go to webrowser http://localhost:8000/
go to webrowser http://localhost:8000/admin
