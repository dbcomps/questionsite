[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# Daily Question Website

This is a simple web application built with Flask that displays a daily question, allows visitors to submit answers, and shows a summary of the most common answers. The website is styled using CSS and includes an admin page for adding new questions.

## Features

- **Daily Question**: Displays a different question each day.
- **Answer Submission**: Allows visitors to submit answers to the daily question.
- **Answer Summary**: Shows a summary of the most common answers.
- **Admin Page**: Enables adding new questions via a web form.
- **Clear Answers**: Allows clearing of all answers for the current question.


## Requirements

- Anaconda/Miniconda
- Python 3.x
- Flask
- SQLite

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/daily-question-website.git
cd daily-question-website
```
### 2. Create a Conda Environment
```bash
conda create --name daily_question_env python=3.9
conda activate daily_question_env
```

### 3. Install Dependencies
```bash
pip install Flask
```
### Initialize the Database
Run the following commands to initialize the SQLite database:
```bash
python
>>> from app import init_db
>>> init_db()
>>> exit()
```
### Run the application
```bash
python app.py
```

Open your web browser and go to http://127.0.0.1:5000/ to see the website.

## Usage

### Main Page
- Visit `http://127.0.0.1:5000/` to see the daily question.
- Submit your answer using the form provided.
- View the summary of answers at the bottom of the page.
- Click the "Clear Answers" button to clear all answers for the current question.

## Admin Page
- Visit `http://127.0.0.1:5000/` add_question to add a new question.
- Fill in the date (YYYY-MM-DD) and the question, then submit the form.

## Project Structure
```
daily-question-website/
│
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── main.js
│
├── templates/
│   ├── add_question.html
│   └── index.html
│
├── app.py
├── database.db
└── README.md
```
- `static/css/styles.css`: CSS file for styling the website.
- `static/js/main.js`: JavaScript file for handling form submissions and clearing answers.
- `templates/`: Contains HTML templates for the main page and admin page.
- `app.py`: Main application file with Flask routes and logic.
- `database.db`: SQLite database file.
- `README.md`: This readme file.

## License

This project is licensed under the MIT License. See the LICENSE file for details.