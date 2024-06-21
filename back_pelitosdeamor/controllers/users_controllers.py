from flask import Flask ,jsonify ,request
from app import app, db,ma
from models.users_models import *

class UserSchema(ma.Schema):
    class Meta:
        fields=('id','name','surname','email','phone', 'password', 'photo', 'type_user')


user_schema=UserSchema()  #Un User
users_schema=UserSchema(many=True) #Multiples user

#--------------------------------------------------------------GET Route USERS

@app.route('/users',methods=['GET'])
def get_Users():
    all_users=User.query.all() 
    result=users_schema.dump(all_users)  
    return jsonify(result)    


@app.route('/users/<id>',methods=['GET'])
def get_user(id):
    user=User.query.get(id)
    return user_schema.jsonify(user)

#--------------------------------------------------------------DELETE Route USERS


@app.route('/users/<id>',methods=['DELETE'])
def delete_user(id):
    user=User.query.get(id)
    db.session.delete(user)
    db.session.commit()                    
    return user_schema.jsonify(user)

#--------------------------------------------------------------POST Route USERS


@app.route('/users', methods=['POST']) 
def create_user():
    name=request.json['name']
    surname=request.json['surname']
    email=request.json['email']
    phone=request.json['phone']
    password=request.json['password']
    photo=request.json['photo']
    type_user=request.json['type_user']

    new_user=User(name, surname, email, phone, password, photo, type_user)
    db.session.add(new_user)
    db.session.commit() 
    return user_schema.jsonify(new_user)


#--------------------------------------------------------------PUT Route USERS


@app.route('/users/<id>' ,methods=['PUT'])
def update_user(id):
    user=User.query.get(id)
 
    user.name=request.json['name']
    user.surname=request.json['surname']
    user.email=request.json['email']
    user.phone=request.json['phone']
    user.password=request.json['password']
    user.photo=request.json['photo']
    user.type_user=request.json['type_user']


    db.session.commit() 
    return user_schema.jsonify(user)
