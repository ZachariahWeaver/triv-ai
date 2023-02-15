from flask import Flask, render_template

app = Flask(__name__)


clues = [["clue 1-1", "clue 1-2", "clue 1-3", "clue 1-4", "clue 1-5", "clue 1-6"],
         ["clue 2-1", "clue 2-2", "clue 2-3", "clue 2-4", "clue 2-5", "clue 2-6"],
         ["clue 3-1", "clue 3-2", "clue 3-3", "clue 3-4", "clue 3-5", "clue 3-6"],
         ["clue 4-1", "clue 4-2", "clue 4-3", "clue 4-4", "clue 4-5", "clue 4-6"],
         ["clue 5-1", "clue 5-2", "clue 5-3", "clue 5-4", "clue 5-5", "clue 5-6"],
         ];


@app.route('/')
def home():
    # generate two 6x6 2D arrays of strings (placeholder text for now)
    categories = ["Cat 1", "Cat 2", "Cat 3", "Cat 4", "Cat 5", "Cat 6"]
    prizes = [0, 200, 400, 600, 800, 1000]

    return render_template('index.html', prizes=prizes, clues=clues, categories=categories)


if __name__ == '__main__':
    app.run(debug=True)


