from app import app, db   #,ma


# defino las tablas
class User(db.Model):   
    __tablename__ = 'users' 

    id=db.Column(db.Integer, primary_key=True) 
    name=db.Column(db.String(100), nullable=False)
    surname=db.Column(db.String(100))
    email=db.Column(db.String(124), unique=True)
    phone=db.Column(db.Integer, nullable=True)
    password=db.Column(db.String(128))
    photo=db.Column(db.String(400))
    type_user=db.Column(db.Boolean, name='Type_user')

    #constructor de la clase user
    def __init__(self,name,surname,email,phone, password, photo, type_user): 
         
        self.name=name
        self.surname=surname
        self.email=email
        self.phone=phone
        self.password=password
        self.photo=photo
        self.type_user=type_user


with app.app_context():
    db.create_all()  
#  ************************************************************