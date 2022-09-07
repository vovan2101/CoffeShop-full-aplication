from . import bp as auth
from flask import jsonify, request


# Create a user
@auth .route('/users', method=['POST'])
def create_user():
    data = request.json
    #check if that is no empty fields
    for field in ['name', 'email', 'phone_number', 'password','home_addres']:
        if field not in data:
            return jsonify({'error': f'You are missing the {field} field'}), 400

    #take data from email field
    email = data('email')
    #Check if email already exist
    user_exist = User.query.filter((User.email == email)).all() ##################
    #If it is exist, return back to the register
    if user_exist:
        return jsonify({'error': f'User with email {email} already exists'}), 400
    #If this email are not exist, create new User
    new_user = User(**data) ########################
    #Put all information we got, to the dictonary
    return jsonify(new_user.to_dict())

