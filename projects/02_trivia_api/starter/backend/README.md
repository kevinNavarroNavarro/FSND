# Backend - Full Stack Trivia API 

### Installing Dependencies for the Backend

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

### Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Review Comment to the Students
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET '/questions'
GET '/categories/<int:category_id>/questions'
POST '/questions'
POST '/quizzes'
DELETE '/questions/<int:id>'

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key: value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}
```

GET '/questions'
- Fetches a dictionary of questions in which the keys are the ids and some values returned is categories, questions, success and total_questions. 
- Request Arguments: None
- Returns: An object with a categories(id, type), questions(answer, category, difficulty, id, question), total_questions and message to success.
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }
  ], 
  "success": true, 
  "total_questions": 3
}
```

GET '/categories/<int:category_id>/questions'
- Fetches a dictionary of questions by category_id in which the keys are the ids and some values returned is success, question, current_category and total_questions. 
- Request Arguments: <int:category_id>
- Returns: An object with a current_categories, questions(answer, category, difficulty, id, question), total_questions and message to success.
{
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 1, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 1, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Maya Angelou", 
      "category": 1, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }
  ], 
  "success": true, 
  "current_category":1
  "total_questions": 3
}
```

POST '/questions'
- General:
    - Creates a new question using the submitted question, answer, category and difficulty. Returns the id of the created question, success value, total questions, and question list based on current page number to update the frontend. 
- `curl -X POST -H "Content-Type: application/json" -d '{"question":"New question", "answer":"answer", "category":1, "difficulty":1}' http://127.0.0.1:5000/questions'`

{
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 1, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 1, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "answer", 
      "category": 1, 
      "difficulty": 1, 
      "id": x, 
      "question": "New question"
    }
  ], 
  "success": true,
  "total_questions": 3
}
```

POST '/questions'
- General:
    - Search a question using the submitted search term. Returns success value, total questions and question list based on current page number to update the frontend. 
{
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 1, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 1, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "answer", 
      "category": 1, 
      "difficulty": 1, 
      "id": x, 
      "question": "New question"
    }
  ], 
  "success": true,
  "total_questions": 3
}
```

POST '/quizzes'
- General:
    - Allow return a different question to previus question using the submitted previous_questions and quiz_category. Returns success value and question list based on category number to update the frontend. 
{
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 1, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }
  ], 
  "success": true
}
```

DELETE '/questions/<int:id>'
- DELETE a question by id
- Request Arguments: id 
- Returns: Returns success value, id deleted question and question list to update the frontend. 
{
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 1, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 1, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "answer", 
      "category": 1, 
      "difficulty": 1, 
      "id": x, 
      "question": "New question"
    }
  ], 
  "success": true,
  "total_questions": 3
```

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
