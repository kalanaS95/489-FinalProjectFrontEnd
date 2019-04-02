CREATE DATABASE iStats;

CREATE TABLE iStats.teams (
  teamID INT NOT NULL,
  teamName VARCHAR(45) NOT NULL,
  managerEmail VARCHAR(45) NOT NULL,
  PRIMARY KEY (teamID)
);


CREATE TABLE iStats.players (
  playerID INT NOT NULL,
  teamID INT NOT NULL,
  playerNumber INT NOT NULL,
  PRIMARY KEY (playerID),
  FOREIGN KEY (teamID) REFERENCES iStats.teams (teamID)
);

CREATE TABLE iStats.games (
  gameID INT NOT NULL,
  teamID INT NOT NULL,
  playerID INT NOT NULL,
  points INT DEFAULT 0,
  FGMade INT DEFAULT 0,
  FGAttempted INT DEFAULT 0,
  FGPercentage REAL DEFAULT 0,
  3FGMade INT DEFAULT 0,
  3FGAttempted INT DEFAULT 0,
  3FGPercentage REAL DEFAULT 0,
  FTMade INT DEFAULT 0,
  FTAttempted INT DEFAULT 0,
  FTPercentage REAL DEFAULT 0,
  offensiveRebounds INT DEFAULT 0,
  defensiveRebounds INT DEFAULT 0,
  totalRebounds INT DEFAULT 0,
  assists INT DEFAULT 0,
  steals INT DEFAULT 0,
  blocks INT DEFAULT 0,
  turnovers INT DEFAULT 0,
  fouls INT DEFAULT 0,

  PRIMARY KEY (gameID,teamID,playerID),
  FOREIGN KEY (playerID) REFERENCES iStats.players(playerID),
  FOREIGN KEY (teamID) REFERENCES iStats.teams(teamID)
);


