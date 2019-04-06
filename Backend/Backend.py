from flask import Flask, jsonify, request
from flask_cors import CORS
import flask_sqlalchemy as sqlalchemy
from sqlalchemy import desc, distinct
import datetime
from passlib.hash import pbkdf2_sha256
from datetime import datetime, timedelta
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
#app.config['SQLALCHEMY_ECHO'] = True

db = sqlalchemy.SQLAlchemy(app)


# ******TABLE CREATION***********

# Creating a table for each team, including the primary key
# teamID, the team name and the manager email
class Teams(db.Model):
    __tablename__ = 'Teams'
    teamID = db.Column(db.Integer, primary_key=True)  # ???
    teamName = db.Column(db.String(50))
    managerEmail = db.Column(db.String(50))
    players = db.relationship('Players', backref='team')


# Creating a table for each player, including the primary key
# playerID, the player number, and a reference to the
# player's teamID
class Players(db.Model):
    __tablename__ = 'Players'
    playerID = db.Column(db.Integer, primary_key=True)
    playerNumber = db.Column(db.Integer, default = 0)
    playerName = db.Column(db.String(50))
    team_id = db.Column(db.Integer, db.ForeignKey(Teams.teamID))
    games = db.relationship('Games',backref='player')


class Game(db.Model):
    __tablename__ = 'Game'
    gameID = db.Column(db.Integer, primary_key=True)
    gameDay = db.Column(db.String(15))
    



# Creating a table for each game, including foreign key
# references to a player ID and their corresponding team ID,
# along with all statistical information such as
# points, rebounds, assists, shooting numbers, etc.
class Games(db.Model):
    __tablename__ = 'Games'
    gameID = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey(Players.playerID))
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

base_url = '/api/'


# ***********Web API routes**************



@app.route(base_url+'addGame', methods=['POST'])
def addGame():
    gameDay = request.get_json().get("Date")
    day = gameDay.split('-')
    myDate = datetime(int(day[0]),int(day[2]),int(day[1]))
    newGame = Game(gameDay=myDate)
    db.session.add(newGame)
    db.session.commit()
    db.session.refresh(newGame)

    return jsonify({"Game day":gameDay, "Success": True}), 200

#addTeam will query the database, specifically the Teams table
#and check whether a team with the same name exists. If not,
#a new team will be added to the Teams table in the database
#with an automatically generated primary key/Team ID
@app.route(base_url+'addTeam', methods=['POST'])
def addTeam():
    #Obtaining variables from the JSON object
    teamName = request.get_json().get('teamName')
    managerEmail = request.get_json().get('managerEmail')
    #Querying the Teams table to see if a team with the same name already exists
    teamCheck = Teams.query.filter_by(teamName=teamName).first();

    if(teamCheck!=None):
        return jsonify({"Success": False,"Error Message":"Duplicate team name"}), 200

    #Creating a new object for the Teams table
    newTeam = Teams(teamName=teamName, managerEmail=managerEmail)

    db.session.add(newTeam)
    db.session.commit()
    db.session.refresh(newTeam)

    return jsonify({"Team Name": teamName, "Manager": managerEmail, "Success": True}), 200



#The addPlayer function requires three arguments, including the player number,
#the player name and the team ID. We query the player table to ensure
#the player name and player number aren't already taken. Also, we query
#the Teams table to ensure the team they are being added to actually exists.
@app.route(base_url+'addPlayer', methods=['POST'])
def addPlayer():
    playerNumber = request.get_json().get('playerNumber')
    playerName = request.get_json().get('playerName')
    team_id = request.get_json().get('teamID')
    
    #We query the players table to ensure the player name hasn't already been added.
    playerCheck = Players.query.filter_by(playerName=playerName).first();
    if(playerCheck!=None):
        return jsonify({"Success": False,"Error Message":"Duplicate player name"}), 200

    #We query the players table to ensure the jersey number hasn't already been added.
    jerseyCheck = Players.query.filter_by(playerNumber=playerNumber).first();
    if(jerseyCheck!=None):
        return jsonify({"Success": False,"Error Message":"Duplicate player number"}), 200

    #We query the Teams table to ensure the player is being added to a team that exists.
    teamCheck = Teams.query.filter_by(teamID=team_id).first();
    if(teamCheck==None):
        return jsonify({"Success": False,"Error Message":"Team ID does not exist"}), 200

    #If all conditions have been passed, we create a new Players object and commit it to the database.
    newPlayer = Players(playerName=playerName, playerNumber=playerNumber, team_id=team_id)

    db.session.add(newPlayer)
    db.session.commit()
    db.session.refresh(newPlayer)

    return jsonify({"Player Name": playerName, "Player Number": playerNumber, "Team ID":team_id, "Success": True}), 200

def main():
    db.create_all()     #Creates the established tables
    app.run()           #Runs the Flask application


if __name__ == '__main__':
    main()
