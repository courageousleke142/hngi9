from flask import Flask, jsonify
result = Flask(__name__)
@result.route('/user_info/')
def get_user_info():
    return jsonify({'slackUsername':'courage_leke',
                    'backend': True,
                    'age': 20,
                    'bio': 'I am a computer science student aiming to be one of the best computer scientist.'})
                   
                    
                    
