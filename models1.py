from flask_sqlalchemy import SQLAlchemy

 
db =SQLAlchemy()

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    players = db.relationship('Players', backref='team')
    
    
 
class Players(db.Model):
   
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    position = db.Column(db.String(), nullable=False)
 
    def __init__(self, team_id,name,age,position):
        self.team_id = team_id
        self.name = name
        self.age = age
        self.position = position
 
    def __repr__(self):
        return f"{self.name}:{self.team_id}"

    


