from . import bp as auth
from flask import jsonify, request
from .models import User
from .http_auth import basic_auth, token_auth


# Create a user
@auth.route('/users', methods=['POST'])
def create_user():
    data = request.json
    #check if that is no empty fields
    for field in ['name', 'email', 'phone_number', 'password','home_addres']:
        if field not in data:
            return jsonify({'error': f'You are missing the {field} field'}), 400

    #take data from email field
    email = data('email')
    #Check if email already exist
    user_exist = User.query.filter((User.email == email)).all() 
    #If it is exist, return back to the register
    if user_exist:
        return jsonify({'error': f'User with email {email} already exists'}), 400
    #If this email are not exist, create new User
    new_user = User(**data)
    #Put all information we got, to the dictonary
    return jsonify(new_user.to_dict())


#Give a token to user, after he logs into his account
@auth.route('/token', methods = ['POST'])
@basic_auth.login_required()
def get_token():
    user = basic_auth.current_user()
    #give a token to user
    token = user.get_token()
    #Return a token as JSON 
    return jsonify({'token': token})



#Get user information from token
@auth.route('/me')
#Making sure that he have a token and logged in
@token_auth.login_required
def me():
    return token_auth.current_user().to_dict()