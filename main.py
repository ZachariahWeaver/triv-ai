import json

from flask import Flask, render_template, redirect  # IMPORT Flask for the web
import pymysql  # to connect to Google Cloud SQL Database (MySQL)
from datetime import date  # For getting the date to keep clue sets daily
from configparser import ConfigParser
import openai  # to connect with Open AI's text generation

config = ConfigParser()  # Take credentials etc. from config file to keep it private and connect to the folowing
config.read('config.ini')

# Open AI
# openai.api_key = config.get('openai', 'SECRET_KEY')

# GCP Cloud SQL Database
cnx = pymysql.connect(
    host=config.get('database', 'MYSQL_HOST'),
    user=config.get('database', 'MYSQL_USER'),
    password=config.get('database', 'MYSQL_PASSWORD'),
    database=config.get('database', 'MYSQL_DB'),
    cursorclass=pymysql.cursors.DictCursor
)

PRIZE_VALUES = [200, 400, 600, 800, 1000]  # these prize numbers are consistent
# GENERATE DAILY SET (GENERATE CATEGORY SET > GENERATE CLUE SET)
# STORE DAILY SET (INSERT CATEGORY SET > INSERT CLUE SET)
# RETRIEVE DAILY SET OR PREVIOUS SET




# def generate_daily_set(day):
#     insert_categories(generate_categories())
#     insert_clues(generate_clues())
#     #         engine=model,
#     #         prompt=prompt,
#     #         temperature=temperature,
#     #         max_tokens=2048,
#     #         n=1,
#     #         stop=None,
#     #         frequency_penalty=0,
#     #         presence_penalty=0
# def generate_categories():
#     #     response = openai.Completion.create()
#     pass
# def generate_clues(prompt, model, temperature=0.5):
#     #     response = openai.Completion.create()
#    pass
# def insert_categories():
#     pass
# def insert_clues(inserts, category_ids):
#     with cnx.cursor() as cursor:
#         for column_index, num in enumerate(category_ids):
#             for sql_index, query in enumerate(inserts):
#                 sql = "INSERT INTO PromptsSchema.clues(clue, response, category_id, ranking) VALUES ('" + str(
#                     query) + "', '" + str(inserts[query]) + "', " + num + ", " + str(sql_index + 1) + ");"
#                 print(sql)
#                 cursor.execute(sql)
#         cnx.commit()
#         cnx.close()
#
# def get_daily_set(day):
#     sql = "SELECT categories.title, clues.clue, clues.response FROM categories INNER JOIN clues ON categories.id = clues.category_id WHERE categories.creation_date = '" + day + "' ORDER BY categories.ranking, clues.ranking;"
#     with cnx.cursor() as cursor:
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         print(result)
app = Flask(__name__)

@app.route('/')
def daily():
    today = '2023-02-22';
    sql = "SELECT categories.title, GROUP_CONCAT(clues.clue SEPARATOR '@@@') AS clues, GROUP_CONCAT(clues.response " \
          "SEPARATOR '@@@') AS responses FROM categories LEFT JOIN clues ON categories.id = clues.category_id WHERE " \
          "categories.creation_date = '" + today + "' GROUP BY categories.title; "
    with cnx.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()

        categories = []
        clues = []
        responses = []

        for r in result:
            categories.append(r['title'])
            clues.append(r['clues'].split("@@@"))
            responses.append(r['responses'].split("@@@"))
        print(categories)
        print(clues)
        print(responses)
    return render_template('index.html', prizes=PRIZE_VALUES, categories=categories, clues=clues, responses=responses)


@app.route('/archive/<int:clue_set_date>')
def archive(clue_set_date):
    if clue_set_date > date.today() or clue_set_date > '2023-22-02':
        redirect('/')
    sql = "SELECT categories.title, GROUP_CONCAT(clues.clue SEPARATOR '@@@') AS clues, GROUP_CONCAT(clues.response " \
          "SEPARATOR '@@@') AS responses FROM categories LEFT JOIN clues ON categories.id = clues.category_id WHERE " \
          "categories.creation_date = '" + clue_set_date + "' GROUP BY categories.title; "
    with cnx.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        categories = []
        clues = []
        responses = []

        for r in result:
            categories.append(r['title'])
            clues.append(r['clues'].split("@@@"))
            responses.append(r['responses'].split("@@@"))
    return render_template('index.html', prizes=PRIZE_VALUES, categories=categories, clues=clues, responses=responses)

#     if clue_set_date > date.today():
#         return redirect('/')
#
# today = clue_set_date category_ids = get_category_ids(today) # ideally fix this so it returns one object and the
# parameters below get passed values from the object
#
# return render_template('index.html', prizes=PRIZE_VALUES, clues=get_clues(category_ids), categories=get_categories(
# category_ids))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)