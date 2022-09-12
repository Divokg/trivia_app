
from operator import truediv
import os
from unicodedata import category
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import random
from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

# Paginate questions 10 per page
def paginate_questions(request, selection):
  page = request.args.get('page',1, type=int)
  start = (page-1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE
  
  questions = [question.format() for question in selection]
  current_questions = questions[start:end]
  
  return current_questions


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app) 
  migrate = Migrate()
  migrate.init_app(app, setup_db)
  
 # Setting up CORS
  cors = CORS(app, resources={r"/api/*" : {"origins":"*"}})
  
 # Home route
  @app.route('/')
  def welcome():
    return jsonify({
      'message': 'insert a request endpoint'
    })
 
 # Setting up Access-Control-Allow
  
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response
  
 # Endpoint to handle GET requests for all available categories.
  
  @app.route('/categories')
  def retrieve_categories():
      #retrieve categories from db
      categories = Category.query.order_by(Category.id).all()
      new_categories = {category.id:category.type for category in categories}
      
      return {
      'categories': new_categories
    }

 # Endpoint to handle GET requests for questions 
 
  @app.route('/questions', methods = ['GET'])
  def retrieve_questions():
    selection = Question.query.order_by(Question.id).all()
    current_questions = paginate_questions(request, selection)
    
    categories=Category.query.order_by(Category.id).all()
    new_categories = {category.id:category.type for category in categories}
    
    return {
      'success': True,
      'questions': current_questions,
      'categories': new_categories,
      'total_questions': len(Question.query.all())
    }
  
  # Endpoint to get specific question by id  
  
  @app.route('/questions/<int:question_id>')
  def get_question_by_id(question_id):
    question = Question.query.get_or_404(question_id)
    
    return{
      'question':question.format()
    }  
  
  
  
  # Endpoint to DELETE question using a question ID. 
  
  @app.route('/delete/<int:question_id>', methods=['DELETE'])
  def delete(question_id):
    question = Question.query.get_or_404(question_id)
    try:
      question.delete()
      
      return {
        'success': True,
        'question deleted': question.format(),
        'deleted': question_id
      }
    
    except:
      abort(422)
    

  # Endpoint to POST a new question, 
 
  @app.route('/add_question', methods=['GET','POST'])
  def create_question():
    form = request.get_json()
    question = Question(question=form.get('question'), answer=form.get('answer'), category= form.get('category'), difficulty=form.get('difficulty'))
        
    try:
       
       question.insert()
       formatted_question = question.format()
      
       return {
        'success': True,
        'created': question.id,
        'question':formatted_question
          
      }
      
    except:
      abort(422) 



 # Endpoint to get questions based on a search term. 
 
  @app.route('/search_questions', methods=['POST'])
  def search_questions():
    body = request.get_json()
    search = body.get('searchTerm', None)
   
    try:
      if search:
        selection = Question.query.order_by(Question.id).filter(Question.question.ilike('%{}%'.format(search)))
        current_questions = paginate_questions(request, selection)
        
        return {
          'success': True,
          'questions': current_questions,
          'total_questions': len(selection.all())
        }
    except:
      abort(404)
        
# Endpoint to get questions based on category. 

  @app.route('/categories/<int:category_id>/questions')
  def retrieve_questions_per_category(category_id):
    questions = Question.query.filter(Question.category == category_id)
    selected_questions = paginate_questions(request, questions)
    
    categories = Category.query.filter(Category.id == category_id)
    selected_categories = paginate_questions(request, categories)
   
    return {
      'questions' : selected_questions,
      'success': True,
      'total_questions': len(selected_questions),
      'current_category':selected_categories
    }
     
  # POST endpoint to get questions to play the quiz. 
    
  @app.route('/play',methods=['POST'])
     
  def quiz_game():
    play_category = request.get_json().get('quiz_category')
    play_previous = request.get_json().get('previous_questions')
    
    try:
      if int(play_category['id']) == 0:
        questions = Question.query.all()
      else:
        questions = (
          Question.query.filter(~Question.id.in_(play_previous)).filter(Question.category == int(play_category['id'])).all()    
        )
      play_questions = [question.format() for question in questions]
      next_question = (random.choice(play_questions)if play_questions else None)
      return {
        'success': True,
        'question': next_question
      }
    except :
      abort(422)
    
    
 # Error handlers for all expected errors 
  @app.errorhandler(404)
  def not_found(error):
    return {
      "success": False,
      "error": 404,
      "message": "resource not found"   
    }, 404
  
  @app.errorhandler(422)
  def unprocessable(error):
    return {
      "success": False,
      "error": 422,
      "message": "unprocessable"   
    }, 422
    
  @app.errorhandler(400)
  def bad_request(error):
    return {
      "success": False,
      "error": 400,
      "message": "bad request"   
    }, 400
    
  @app.errorhandler(405)
  def method_not_allowed(error):
    return {
      "success": False,
      "error": 405,
      "message": "method not allowed"   
    }, 405
    
  @app.errorhandler(500)
  def server_error(error):
    return {
      "success": False,
      "error": 500,
      "message": "server error"   
    }, 500
  
  return app



    