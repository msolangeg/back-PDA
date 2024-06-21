from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from sqlalchemy import Column, Integer, String, Float, ForeignKey


app=Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/pda_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False 


db= SQLAlchemy(app)
ma=Marshmallow(app) 

from controllers.users_controllers import *
from controllers.pets_controllers import *


if __name__=='__main__':  
    app.run(debug=True, port=5000)

