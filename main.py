from flask import Flask, render_template
import pymysql
from datetime import date
from configparser import ConfigParser
import openai

config = ConfigParser()
config.read('config.ini')
# openai.api_key = config.get('openai', 'SECRET_KEY')

# Test your authentication
# models = openai.Model.list()
# print(models)
cnx = pymysql.connect(
    host=config.get('database', 'MYSQL_HOST'),
    user=config.get('database', 'MYSQL_USER'),
    password=config.get('database', 'MYSQL_PASSWORD'),
    database=config.get('database', 'MYSQL_DB'),
    cursorclass=pymysql.cursors.Cursor
)

clues = [["a", "b", "c", "d", "e"],
         ["f", "g", "h", "i", "j"],
         ["k", "l", "m", "n", "o"],
         ["p", "q", "r", "s", "t"],
         ["u", "v", "w", "x", "y"]]

responses = [["", "", "", "", ""],
             ["", "", "", "", ""],
             ["", "", "", "", ""],
             ["", "", "", "", ""],
             ["", "", "", "", ""]]

categories = ["", "", "", "", "", ""]
category_ids = [0, 0, 0, 0, 0, 0]

# with cnx.cursor() as cursor:
#     sql = #"INSERT INTO PromptsSchema.clues(clue, response, category_id, ranking)VALUES ('This scientist made groundbreaking discoveries in the field of primatology and was the subject of a famous National Geographic documentary', 'Jane Goodall', '2', '5');"
#     cursor.execute(sql)
#     cnx.commit()
#     cnx.close()

# with cnx.cursor() as cursor:
#     sql = "SELECT name, id from categories WHERE day = '" + str(date.today()) + "'"
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     for index, row in enumerate(result):
#         categories[index] = row[0]
#         category_ids[index] = row[1]
#
# with cnx.cursor() as cursor:
#     for column_index, num in enumerate(category_ids):
#
#         sql = "SELECT clue, response FROM clues WHERE category_id = '" + str(num) + "'"
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         for row_index, row in enumerate(result):
#             print(column_index)
#             print(row_index)
#             clues[row_index][column_index] = row[0]
#             responses[row_index][column_index] = row[1]
#             print(row[0])
#             print(row[1])

prizes = [0, 200, 400, 600, 800, 1000]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', prizes=prizes, clues=clues, responses=responses, categories=categories)


# change to a home file as landing spot


@app.route('/daily')
def daily():
    code = date.today()
    # generate two 6x6 2D arrays of strings (placeholder text for now)
    return render_template('index.html', prizes=prizes, clues=clues, categories=categories)


@app.route('/archive/<int:clue_id>')
def archive():
    # generate two 6x6 2D arrays of strings (placeholder text for now)
    # query database for questions from this day. if no database table exists
    return render_template('index.html', prizes=prizes, clues=clues, categories=categories, game_id=variable)


# def generate_text(prompt, model=, temperature=0.5):
#     response = openai.Completion.create(
#         engine=model,
#         prompt=prompt,
#         temperature=temperature,
#         max_tokens=2048,
#         n=1,
#         stop=None,
#         frequency_penalty=0,
#         presence_penalty=0
#     )

if __name__ == '__main__':
    app.run(debug=True)

# TODOLIST: Fix clue validation and score keeping. Set up clue/category generation, setup
