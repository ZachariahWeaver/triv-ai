import pymysql
from flask import Flask, render_template, redirect, url_for
from datetime import date
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
FIRST_DATE = date(2023, 5, 28)

app = Flask(__name__)


def fetch_clueset(clueset_number):
    
    sql = "SELECT categories.title, GROUP_CONCAT(clues.clue SEPARATOR '@@@') AS clues, GROUP_CONCAT(clues.response " \
          "SEPARATOR '@@@') AS responses FROM categories LEFT JOIN clues ON categories.id = clues.category_id WHERE " \
          "categories.clueset_number = '" + str(clueset_number) + "' GROUP BY categories.title;"
    
    cnx = pymysql.connect(user=db_user, password=db_password, host=db_host, db=db_name)
    with cnx.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
    cnx.close()

    return result

@app.route('/')
def weekly():
    today = date.today() #'2023-02-22'
    current_num = (today - FIRST_DATE).days//7

    clueset = fetch_clueset(current_num)
    categories = []
    clues = []
    responses = []


    for r in clueset:
        categories.append(r[0])
        clues.append(r[1].split("@@@"))
        responses.append(r[2].split("@@@"))

    return render_template('index.html', prizes=PRIZE_VALUES, categories=categories, clues=clues, responses=responses, clueset_num=current_num, current_num=current_num)

@app.route('/archive/<int:clueset_num>')
def archive(clueset_num):
    today = date.today()

    current_num = (today - FIRST_DATE).days//7
    if (clueset_num < 0 or clueset_num >= current_num): #change to < 1 after testing
        print("redirect less than")
        return redirect(url_for('weekly'))

    clueset = fetch_clueset(clueset_num)

    categories = []
    clues = []
    responses = []


    for r in clueset:
        categories.append(r[0])
        clues.append(r[1].split("@@@"))
        responses.append(r[2].split("@@@"))
    return render_template('index.html', prizes=PRIZE_VALUES, categories=categories, clues=clues, responses=responses, clueset_num=clueset_num, current_num=current_num)

if __name__ == '__main__':  #remove these lines for deployment to PythonAnywhere 
    app.run(debug=True, use_reloader=False) 