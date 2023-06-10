# Triv-AI

Triv-AI is a Trivia Game Show inspired web application, offering an interactive and engaging trivia gaming experience. Built using JavaScript for the frontend, Python and Flask for the backend, and MySQL for data storage, Triv-AI provides an exciting user interface where users can play and interact. The distinguishing feature of Triv-AI is its planned integration with OpenAI's API to generate clues, giving a unique AI-powered twist to the classic trivia game format.

## Frontend

Written in JavaScript, HTML, and CSS, the frontend interface provides a grid layout showcasing the categories and clues, and displays an active clue section when clues are selected. The frontend implements game functionalities like revealing and hiding clues, accepting user answers, initiating and stopping a timer for each clue, and maintaining the user's score.

## Backend

Powered by Flask, the backend application connects the frontend and the MySQL database. It retrieves data from the database and serves the game web pages to the user. There are separate routes defined for weekly and archive games. Each route fetches a unique set of categories and clues, derived based on the date and time.

## Database

The MySQL database hosts the game's categories and clues. Each category and its associated clues form a "clueset", which can be retrieved and displayed on the frontend to cater to the game's requirements.

## OpenAI Integration

An exciting feature that sets Triv-AI apart is the proposed integration with OpenAI's API. This integration will facilitate the automatic generation of clues, rendering the game more dynamic and challenging. The inclusion of AI in generating clues ensures a steady influx of new and unpredictable clues, thereby maintaining user engagement.

## Configuration and Deployment

The application's configuration settings, such as database credentials, are securely housed in a `config.ini` file. The application can be run locally during development and testing, or deployed on a web server or a cloud platform compatible with Python and Flask applications.

---

![Triv-AI logo](/static/screenshot.png)
