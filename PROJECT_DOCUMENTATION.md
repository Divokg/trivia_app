## Udacitrivia 

This is a project that shows both my API and API documentation skills to build a trivia API.


# Getting Started
Developers using this project should already have python3, pip and node installed on their local machines.


# Backend

Run pip install requirements.txt from the backend folder. All erequired packages are included in the requirements file.

Run the following commands:

export FLASK_APP=flaskr
export FLASK_ENV=development
flask run

These commands put the application in development and directs your application to use the __init__.py file in your flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made.

By default the application is run on http://127.0.0.1:5000/ which is a proxy in the frontend configuration.

## Frontend

Run the following commands from the frontend folder.

npm install // only once to install dependencies
npm start 

The frontend will run on localhost:3000.

# Tests

To run tests move to the backend folder and run the following commands:

dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py

When you run this commands for the first time omit the dropdb command.



# API Reference

# Getting Started
--Authentication: This version of the application does not require API Keys or authentication
--Base URL: This app can only run locally and is not hosted as a base URL.
The backend app is hosted at http://127.0.0.1:5000/, this is set as a proxy in the frontend configuration 

# Error Handling

Errors are returned as JSON objects in the following format:

{
    "success": False,
    "error": 404,
    "message": "resource not found"   
}

The API will return four error types when requests fail:
 404: Resource Not Found
 400: Bad Request
 422: Not Processable
 405: Method not allowed


 ## Endpoints

 # GET /questions

 --General:
 Returns a list of category objects, a list of question objects, success value and total number of questions.
 Results are paginated in groups of 10. Also include a request argument to choose page number, starting from 1.
 Sample: curl http://127.0.0.1:5000/questions

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
"answer": "Edward Scissorhands",
"category": 5,
"difficulty": 3,
"id": 6,
"question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
},
{
"answer": "Muhammad Ali",
"category": 4,
"difficulty": 1,
"id": 9,
"question": "What boxer's original name is Cassius Clay?"
},
{
"answer": "Brazil",
"category": 6,
"difficulty": 3,
"id": 10,
"question": "Which is the only team to play in every soccer World Cup tournament?"
},
{
"answer": "Uruguay",
"category": 6,
"difficulty": 4,
"id": 11,
"question": "Which country won the first ever soccer World Cup in 1930?"
},
{
"answer": "George Washington Carver",
"category": 4,
"difficulty": 2,
"id": 12,
"question": "Who invented Peanut Butter?"
},
{
"answer": "Lake Victoria",
"category": 3,
"difficulty": 2,
"id": 13,
"question": "What is the largest lake in Africa?"
},
{
"answer": "The Palace of Versailles",
"category": 3,
"difficulty": 3,
"id": 14,
"question": "In which royal palace would you find the Hall of Mirrors?"
},
{
"answer": "Agra",
"category": 3,
"difficulty": 2,
"id": 15,
"question": "The Taj Mahal is located in which Indian city?"
}
],
"success": true,
"total_questions": 31
}


# POST /questions
--General:
Creates a new question using the submitted question, answer, difficulty and category. 

curl http://127.0.0.1:5000/questions?page=2 -X POST -H "Content-Type: application/json" -d '{"question":"Who made the first plane", "answer":"The Wright Brothers", "category":"1", "difficulty":"2"}'

{
  "created": 38,
  "questions": [
    {
      "answer": "The Wright Brothers",
      "category": ,1
      "difficulty": 2,
      "id": 38,
      "question": "Who made the first plane"
    }
    ],
    "created": 38,
  "success": true,
  "total_books": 32
}


# DELETE /questions/{question_id}

General:
Deletes the question of the given ID if it exists. Returns the id of the deleted question, success value, total questions, and question list based on current page number to update the frontend.
curl -X DELETE http://127.0.0.1:5000/questions/4?page=1


{
  "deleted": 4,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"     
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }
  ],
  "success": true,
  "total_questions": 31
}


# Authors

Samuel Ndungu Njoroge

# Acknowledgements

The awesome Tutors and Teachers at Udacity