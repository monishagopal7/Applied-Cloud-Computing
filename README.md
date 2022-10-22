**Terminal Steps**

docker compose up -build 
#Need to run for the first time

docker compose up


**pgAdmin adi URL as below**

http://localhost:5050/login?next=%2F

username: admin@email.com

password :admin



**To create the server inside pdAdmin**

Click Add new server-> Under General (hostname=db) -> Under Connection (hostname=db) (username=postgres) (Password=postgres)

name: db

-username: postgres

-password: postgres



*to find the table created*

in pdAdmin go to Server->db->DataBases->db->Schemas->Tables->run query(SELECT item_name, price
	FROM public.food_menu_items;)




**Reference**

https://www.youtube.com/watch?v=eKEzq59FhEw

https://github.com/Chensokheng/psql-docker/blob/master/docker-compose.yml

https://stackoverflow.com/questions/37259584/postgres-shuts-down-immediately-when-started-with-docker-compose/71315084#71315084

https://www.postgresqltutorial.com/postgresql-python/connect/


https://stackoverflow.com/questions/57720565/flask-sqlalchemy-neither-sqlalchemy-database-uri-nor-sqlalchemy-binds-is-set-d
https://dba.stackexchange.com/questions/75214/postgresql-not-running-on-mac

https://stackoverflow.com/questions/64985913/failed-to-solve-with-frontend-dockerfile


https://www.youtube.com/watch?v=TngMltxom5E


https://support.codefresh.io/hc/en-us/articles/360016685419-Postgres-LOG-received-fast-shutdown-request-after-initialization


https://www.reddit.com/r/docker/comments/qy5x3j/docker_entrypointinitdbd_postgres/


https://superuser.com/questions/1390250/volumes-type-is-a-required-property-when-running-docker-compose
