from flask import Flask,render_template,jsonify,request
import json
import random
import os
import psycopg2  #to establish connection with the postgres db

app = Flask(__name__)

#establishing the connection
conn = psycopg2.connect( 
    database = os.environ.get('POSTGRES_DB'),     #"db"
    user = os.environ.get('POSTGRES_USER'),    #"postgres",
    password = os.environ.get('POSTGRES_PASSWORD'), #"postgres"
    host = os.environ.get('DB_HOST'), #"db",
    port = os.environ.get('DB_PORT')  #"5432"
    )
#Executing an MYSQL function using the execute() method
@app.route('/api/pickrandom/',methods=[ 'GET'])
def week5():
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    select_stmt = "SELECT item_name, price FROM food_menu_items ORDER BY random() LIMIT 1" # item_name #food

    cursor.execute(select_stmt)
    while True:
        try:
            cursor.execute(select_stmt)
            break

        except Exception as e:
            print(e.message)

    res =list(cursor.fetchone())
    #cursor.close()
    # conn.close()
    return jsonify({res[0]:res[1]})
        
@app.route('/')
def landingpage():
    return render_template('index.html')

@app.route("/api/food-menu",methods = ['GET']) 
def complete_menu():
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    select_stmt = "SELECT * FROM food_menu_items"
    cursor.execute(select_stmt)

    return jsonify(cursor.fetchall())

    

if __name__ == "__main__":
    #  app.run('0.0.0.0', port=5000,debug=True)
    port=os.environ.get('API_PORT')
    app.run('0.0.0.0',port=port,debug=True)

