from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # generate two 6x6 2D arrays of strings (placeholder text for now)
    categories = ["Cat 1","Cat 2","Cat 3","Cat 4","Cat 5","Cat 6"]
    prizes = [0,200,400,600,800,1000]
    clues = [['{}{}'.format(1+i, 1+j) for j in range(6)] for i in range(6)]
    return render_template('index.html', prizes=prizes, clues=clues, categories = categories)

if __name__ == '__main__':
    app.run(debug=True)
