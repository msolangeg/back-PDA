from app import app, db   #,ma
from sqlalchemy import Column, ForeignKey, Integer, String, Float

# Si quiero realizar un cruce de tablas debo utilizar:
# from sqlalchemy.orm import declarative_base, relationship

# defino las tablas
class Pet(db.Model):
    __tablename__ = 'pets' 

    id = Column(Integer, primary_key=True) 
    name = Column(String(100))
    description = Column(String(255))  
    photo = Column(String(255))  
    weight = Column(Float) 
    breed = Column(String(100)) 
    age = Column(Integer)

    #constructor de la clase pet
    def __init__(self,name,description,photo,weight,breed,age):

        self.name=name
        self.description=description
        self.photo=photo
        self.weight=weight
        self.breed=breed
        self.age=age

with app.app_context():
    db.create_all()  # aqui crea todas las tablas si es que no estan creadas
#  ************************************************************