from flask import Flask
from app import app
from app import classClass
from flask_sqlalchemy import SQLAlchemy
import random

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column("id", db.Integer, primary_key=True, nullable=False)
    username=db.Column("username", db.String(100), nullable=False)
    class1=db.Column("class1", db.String(300), nullable=False)

    def convertStringToClass(self):
        """
        Converts the string reprensentation of the class in to an actual class
        object and returns it.
        """

        try:
            res=classClass.Class()
            res.loadFromString(self.class1)
            return res
        except:
            print("String cannot be converted to a class object")
            return "String cannot be converted to a class object"
    
    @staticmethod
    def generateID():
        """
        Generates a random 5 digit integer that should be used as an ID for the
        users in the database and returns it.
        """

        try:
            tempId=random.randint(10000,99999)
            name=User.query.filter_by(id=tempId).first()
            if name==None:
                return tempId
            else:
                return User.generateID()
        except:
            print("Not enough unused ID's in the database")
            return "Not enough unused ID's in the database"

    def __repr__(self):
        """
        Returns a string representation of the User including their name, classes,
        and ID.
        """

        return "Username:    "+self.username+" Class:    "+self.class1+" ID:    "+str(self.id)

def getDB():
    """
    Returns the instance of the database being used by this file.
    """

    return db

def addToDB(name, c):
    """
    Adds a new entry to the database using a username, class, and
    generating a new random ID.
    """
    try:
        db.session.add(User(id=User.generateID(), username=name, class1=c.convertToString()))
        db.session.commit()
        return "Successfully added to database"
    except:
        print("Error adding to database")
        return "Error adding to database"

def pullByID(num):
    """
    Returns the user account with the ID passed as an argument
    (if no account matches the ID then None is returned)
    """

    val=User.query.filter_by(id=num).first()
    if val==None:
        print("No account has the ID: " + str(num))
        
    return val

def pullByUsername(name):
    """
    Returns all users with the username passed as an argument
    (if no account matches the username then [] is returned)
    """

    val=User.query.filter_by(username=name).all()
    if val==[]:
        print("No account has the username: " + name)

    return val