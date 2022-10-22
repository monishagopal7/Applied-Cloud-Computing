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
