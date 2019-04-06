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
    playerNumber = db.Column(db.Integer)
    team_id = db.Column(db.Integer, db.ForeignKey(Teams.teamID))
    games = db.relationship('Games',backref='player')
    # teamID= db.relationship('Teams', backref = 'Players', lazy = T rue)          #???


# Creating a table for each game, including foreign key
# references to a player ID and their corresponding team ID,
# along with all statistical information such as
# points, rebounds, assists, shooting numbers, etc.



    #playerID = db.relationship('Players', backref='Games', lazy=True)  # ???
    #teamID = db.relationship('Teams', backref='Games', lazy=True)  # ???
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


@app.route(base_url+'addTeam', methods=['POST'])
def addTeam():
    teamName = request.get_json().get('teamName')
    managerEmail = request.get_json().get('managerEmail')

    newTeam = Teams(teamName=teamName, managerEmail=managerEmail)

    db.session.add(newTeam)
    db.session.commit()

    db.session.refresh(newTeam)

    return jsonify({"Team Name": teamName, "Manager": managerEmail, "Success": True}), 200


def main():
    db.create_all()  # Creates the established tables
    app.run()  # Runs the Flask application


if __name__ == '__main__':
    main()
