from flask import Flask, jsonify, request
from flask_cors import CORS
import flask_sqlalchemy as sqlalchemy
from sqlalchemy import desc, distinct
import datetime
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
#app.config['SQLALCHEMY_ECHO'] = True

db = sqlalchemy.SQLAlchemy(app)




#******TABLE CREATION***********

#Creating a table for each team, including the primary key
#teamID, the team name and the manager email
class Teams(db.Model):
    __tablename__ = 'Teams'
    teamID = db.Column(db.Integer, primary_key=True)                            #???
    teamName = db.Column(db.String(50))
    managerEmail = db.Column(db.String(50))

#Creating a table for each player, including the primary key
#playerID, the player number, and a reference to the
#player's teamID
class Players(db.Model):
    __tablename__ = 'Players'
    playerID = db.Column(db.Integer, primary_key=True)
    teamID= db.relationship('Teams', backref = 'Players', lazy = True)          #???   
    playerNumber = db.Column(db.Integer)

#Creating a table for each game, including foreign key
#references to a player ID and their corresponding team ID,
#along with all statistical information such as
#points, rebounds, assists, shooting numbers, etc.
class Games(db.Model):
    __tablename__ = 'Games'
    gameID = db.Column(db.Integer, primary_key=True)                        
    playerID= db.relationship('Players', backref = 'Games', lazy = True)        #???
    teamID= db.relationship('Teams', backref = 'Games', lazy = True)            #???
    points = db.Column(db.Integer)
    FGMade = db.Column(db.Integer)
    FGAttempted = db.Column(db.Integer)
    FGPercentage = db.Column(db.Float)
    threesAttempted = db.Column(db.Integer)
    threesMade = db.Column(db.Integer)
    threesPercentage = db.Column(db.Float)
    FTMade = db.Column(db.Integer)
    FTAttempted = db.Column(db.Integer)
    FTPercentage = db.Column(db.Float)
    offensiveRebounds = db.Column(db.Integer)
    defensiveRebounds = db.Column(db.Integer)
    totalRebounds = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    steals = db.Column(db.Integer)
    blocks = db.Column(db.Integer)
    turnovers = db.Column(db.Integer)
    fouls = db.Column(db.Integer)




def main():
    db.create_all()     #Creates the established tables
    app.run()           #Runs the Flask application



if __name__ == '__main__':
    main()
