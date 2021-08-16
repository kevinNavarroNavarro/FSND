import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_question(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    CORS(app, resources={'/': {'origins': '*'}})

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods','GET,PUT,POST,DELETE,OPTIONS')
        return response

    '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
    @app.route('/categories', methods=["GET"])
    def retrieve_categories():
      if request.method == "GET":
        categoriesdb = Category.query.all()
        categories = {}
                
        for categ in categoriesdb:
          categories[categ.id] = categ.type

        if len(categories) == 0:
              abort(404)
          
        return jsonify({
            'success': True,
            'categories': categories
          })

    '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
    @app.route('/questions', methods=["GET"])
    def retrieve_questions():
      if request.method == "GET":
        selection = Question.query.order_by(Question.id).all()
        current_questions = paginate_question(request, selection)
        
        if len(current_questions) == 0:
            abort(404)

        categoriesdb = Category.query.order_by(Category.id).all()
        categories = {}

        for categ in categoriesdb:
          categories[categ.id] = categ.type

        return jsonify({
          'success': True,
           'categories': categories,
           'questions': current_questions,
           'total_questions': len(selection)
          })

    '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
    @app.route('/questions/<int:id>', methods=['DELETE'])
    def delete_question(id):
      if request.method == "DELETE":
        try:
            question = Question.query.filter(Question.id==id).one_or_none()

            if question is None:
                abort(404)

            question.delete()

            return jsonify({
                'success': True,
                'deleted': id,
                'total_questions': len(Question.query.all())
            })
        except:
            abort(422)

    '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''

    '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
    @app.route('/questions', methods=['POST'])
    def create_question_and_search():
      if request.method == "POST":
        body = request.get_json()

        searchTerm = body.get('searchTerm', None)
        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        new_category = body.get('category', None)
        new_difficulty = body.get('difficulty', None)

        try:
            if searchTerm:
                selection = Question.query.filter(Question.question.ilike(f"%{searchTerm}%")).all()
                current_questions = paginate_question(request, selection)

                return jsonify({
                    'success': True,
                    'questions': current_questions,
                    'total_questions': len(current_questions)
                })
            else:
                question = Question(question=new_question, answer=new_answer,
                                    category=new_category, difficulty=new_difficulty)
                question.insert()

                selection = Question.query.order_by(Question.id).all()
                current_questions = paginate_question(request, selection)

                return jsonify({
                    'success': True,
                    'question_created': question.question,
                    'created': question.id,
                    'questions': current_questions,
                    'total_questions': len(Question.query.all())
                })

        except:
            abort(422)

    '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
    @app.route('/categories/<int:category_id>/questions', methods=["GET"])
    def retrieve_questions_by_category(category_id):
      if request.method == "GET":
        category = Category.query.filter_by(id=category_id).one_or_none()
        
        if category is None:
          abort(404)

        try:
          selection = Question.query.filter(Question.category == category_id)
          current_questions = paginate_question(request, selection)

          if len(current_questions) == 0:
              abort(404)

          return jsonify({
            'success': True,
            'questions': current_questions,
            'current_category': category.type,
            'total_questions': len(Question.query.all())
            })
        except: 
          abort(400)

    '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
    @app.route('/quizzes', methods=['POST'])
    def play_quiz():
      if request.method == "POST":
        try:
          body = request.get_json()
          previus_questions = body.get('previous_questions', None)
          category = body.get('quiz_category', None)

          category_id = category['id']
          next_question = None
                  
          if category_id != 0:
            av_questions = Question.query.filter(Question.category==category_id).filter(Question.id.notin_(previus_questions)).all()    
          else:
            av_questions = Question.query.filter(Question.id.notin_(previus_questions)).all()
                  
          if len(av_questions) > 0:
            next_question = random.choice(av_questions).format()
                  
          return jsonify({
            'success': True,
            'question': next_question
            })
        
        except:
          abort(422)
          
    '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 500

    @app.errorhandler(405)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed"
        }), 405

    return app