from flask import Flask, render_template
import pymysql
from datetime import date
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

cnx = pymysql.connect(
    host=config.get('database', 'MYSQL_HOST'),
    user=config.get('database','MYSQL_USER'),
    password=config.get('database','MYSQL_PASSWORD'),
    database=config.get('database','MYSQL_DB'),
    cursorclass=pymysql.cursors.DictCursor
)

with cnx.cursor() as cursor:
    sql = "SELECT * FROM categories"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)
cnx.close()

clues = [
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
]
categories = ["", "", "", "", "", ""]
prizes = [0, 200, 400, 600, 800, 1000]


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/daily')
def daily():
    code = date.today()
    # generate two 6x6 2D arrays of strings (placeholder text for now)
    return render_template('daily.html', prizes=prizes, clues=clues, categories=categories)


@app.route('/archive/<int:clue_id>')
def archive():
    # generate two 6x6 2D arrays of strings (placeholder text for now)
    # query database for questions from this day. if no database table exists
    return render_template('daily.html', prizes=prizes, clues=clues, categories=categories, game_id=variable)


if __name__ == '__main__':
    app.run(debug=True)

# TODOLIST: Fix clue validation and score keeping. Set up clue/category generation, setup
