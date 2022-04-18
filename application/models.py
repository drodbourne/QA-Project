from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError

 

class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(30), nullable=False)
    players = db.relationship('Players', backref='team',passive_deletes=True)

    def __repr__(self):
        return 'Choose {}'.format(self.team_name)

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    position = db.Column(db.String(20), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id',ondelete='CASCADE'), nullable=False)


class AddTeamForm(FlaskForm):
    team_name = StringField('Enter the team name',validators=[DataRequired()])
    submit = SubmitField('Add Team')

class UpdateTeamForm(FlaskForm):
    team_name = StringField('Update the team name',validators=[DataRequired()])
    submit = SubmitField('Update Team')

class AddPlayerForm(FlaskForm):
    team_id = IntegerField('team_id')
    name = StringField('Enter Name', validators=[DataRequired()])
    age = IntegerField('Enter Age', validators=[DataRequired()])
    team_name = SelectField (u'Select Team', choices = [])

    position = SelectField("Select Position", choices=[
        ("goalkeeper", "Goalkeeper"), 
        ("defense", "Defense"),
        ("midfield", "Midfield"), 
        ("forward", "Forward")
        ])

    submit = SubmitField('Add Player')

class UpdatePlayerForm(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    position = SelectField("position", choices=[
        ("goalkeeper", "Goalkeeper"), 
        ("defense", "Defense"),
        ("midfield", "Midfield"), 
        ("forward", "Forward")
        ])

    submit = SubmitField('Update Player')



    
    
 


