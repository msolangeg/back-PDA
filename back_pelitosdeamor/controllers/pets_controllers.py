from flask import Flask ,jsonify ,request
from app import app, db,ma
from models.pets_models import *

class PetSchema(ma.Schema):
    class Meta:
        fields=('id', 'name', 'description', 'photo', 'weight', 'breed', 'age')

#Realizo los esquemas para traer uno o mas pets

pet_schema=PetSchema() #Solo uno
pets_schema=PetSchema(many=True) #Multiples


#--------------------------------------------------------------GET Route PETS 

@app.route('/pets',methods=['GET'])
def get_Pets():
    all_pets=Pet.query.all()
    result=pets_schema.dump(all_pets)
    return jsonify(result)



@app.route('/pets/<id>',methods=['GET'])
def get_pet(id):
    pet=Pet.query.get(id)
    return pet_schema.jsonify(pet)

#--------------------------------------------------------------DELETE Route PETS 

@app.route('/pets/<id>',methods=['DELETE'])
def delete_pet(id):
    pet=Pet.query.get(id)
    db.session.delete(pet)
    db.session.commit()
    return pet_schema.jsonify(pet)

#--------------------------------------------------------------POST Route PETS 

@app.route('/pets', methods=['POST'])
def create_pet():
    
    name=request.json['name']
    description=request.json['description']
    weight=request.json['weight']
    breed=request.json['breed']
    age=request.json['age']
    photo=request.json['photo']
  

    new_pet=Pet(name, description, photo, weight, breed, age)
    db.session.add(new_pet)
    db.session.commit()
    return pet_schema.jsonify(new_pet)

#--------------------------------------------------------------PUT Route PETS 

@app.route('/pets/<id>' ,methods=['PUT'])
def update_pet(id):
    pet=Pet.query.get(id)
 
    pet.name=request.json['name']
    pet.description=request.json['description']
    pet.weight=request.json['weight']
    pet.breed=request.json['breed']
    pet.age=request.json['age']
    pet.photo=request.json['photo']
   
    db.session.commit()
    return pet_schema.jsonify(pet)
