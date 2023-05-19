import os
import pymysql
from flask import Flask, render_template, request

import configparser

# Load configuration from the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

database_credentials = 'local_database'     #change this variable to 'pythonanywhere' for deployment to PythonAnywhere 
db_user = config.get(database_credentials, 'db_user')
db_password = config.get(database_credentials, 'db_password')
db_name = config.get(database_credentials, 'db_name')
db_host = config.get(database_credentials, 'db_host')


PRIZE_VALUES = [200, 400, 600, 800, 1000]

app = Flask(__name__)

@app.route('/')
def daily():
    today = '2023-02-22'
    sql = "SELECT categories.title, GROUP_CONCAT(clues.clue SEPARATOR '@@@') AS clues, GROUP_CONCAT(clues.response " \
          "SEPARATOR '@@@') AS responses FROM categories LEFT JOIN clues ON categories.id = clues.category_id WHERE " \
          "categories.creation_date = '" + today + "' GROUP BY categories.title; "
    cnx = pymysql.connect(user=db_user, password=db_password, host=db_host, db=db_name)

    with cnx.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()

    cnx.close()

    categories = []
    clues = []
    responses = []
    print(result)
    for r in result:
        categories.append(r[0])
        clues.append(r[1].split("@@@"))
        responses.append(r[2].split("@@@"))
    
    print(categories)
    print(clues)
    print(responses)

    return render_template('index.html', prizes=PRIZE_VALUES, categories=categories, clues=clues, responses=responses)

@app.route('/archive/<int:clue_set_date>')
def archive(clue_set_date):
    # You can implement this function similarly to the `daily()` function.
    pass


if __name__ == '__main__':  #remove these lines for deployment to PythonAnywhere 
    app.run(debug=True, use_reloader=False) 