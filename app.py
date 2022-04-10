from flask import Flask,render_template,request,redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError


from models import db, Team, Players
 
app = Flask(__name__)
app = Flask(__name__, template_folder='templates')
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
db.init_app(app)





class TeamForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2,max=30)])
    submit = SubmitField('Add Team')

class PlayerForm(FlaskForm):
    team_id = IntegerField('team_id')
    name = StringField('Name', validators=[DataRequired(), Length(min=2,max=40)])
    age = IntegerField('Age', validators=[DataRequired(), Length(min=1,max=3)])
    position = SelectField("position", choices=[
        ("goalkeeper", "Goalkeeper"), 
        ("defense", "Defense"),
        ("midfield", "Midfield"), 
        ("forward", "Forward")
        ])

    submit = SubmitField('Save')

class UpdateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2,max=40)])
    age = IntegerField('Age', validators=[DataRequired(), Length(min=1,max=3)])
    position = SelectField("position", choices=[
        ("goalkeeper", "Goalkeeper"), 
        ("defense", "Defense"),
        ("midfield", "Midfield"), 
        ("forward", "Forward")
        ])
    submit = SubmitField('Update Player')

def getTeamID():
    emp_str = ""
    new_string = "".join(str(Team.query.order_by(Team.id.desc()).limit(1).all()))
    
    for m in new_string:
        if m.isdigit():
            emp_str = emp_str + m

    mteam_id = int(emp_str)
    return mteam_id

def getTeamName(id):
    team = Team.query.filter_by(id=id).first()
    return team.name


def teamCount():
    number_of_teams = Team.query.count()
    return number_of_teams

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('team.html')

@app.route('/team' , methods = ['GET','POST'])
def teamcreate():
    
    form = TeamForm()
    teams = Team.query.all()
    
    if request.method == 'GET':
        return render_template('team.html',form=form,output_data = teams )
 
    if request.method == 'POST':
        
        name = request.form['name']
        team = Team(name=name)
        db.session.add(team)
        db.session.commit()
        
        return redirect('/data/addplayer')
        
        
 
@app.route('/data/addplayer' , methods = ['GET','POST']) 
def playercreate():
    
    mteam_id = getTeamID()
    strTeam = getTeamName(mteam_id)
    
    form = PlayerForm()
    if request.method == 'GET':
        return render_template('addplayer.html',form=form,variable1=mteam_id,variable2=strTeam)
 
    if request.method == 'POST':
        team_id = mteam_id
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        player = Players(team_id=team_id, name=name, age=age, position = position)
        db.session.add(player)
        db.session.commit()
        return redirect('/data')
 
 
@app.route('/data')
def RetrieveList():
    mteam_id = getTeamID()
    
    players = Players.query.filter_by(team_id=mteam_id)
    return render_template('datalist.html',output_data = players)
 
 
@app.route('/data/<int:id>')
def RetrievePlayers(id):
    player = Players.query.filter_by(id=id).first()
    if player:
        return render_template('data.html', player = player)
    return f"Player with id ={id} Doenst exist"

    
 
 
@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    player = Players.query.filter_by(id=id).first()
    form = UpdateForm()
       
    
    if request.method == 'POST':
        if player:
            player.name = request.form['name']
            player.age = request.form['age']
            player.position = request.form['position']

            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Player with id = {id} Does not exist"
 
    return render_template('update.html',form=form,player = player)
 
 
@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    player = Players.query.filter_by(id=id).first()
    if request.method == 'POST':
        if player:
            db.session.delete(player)
            db.session.commit()
            return redirect('/data')
        abort(404)
 
    return render_template('delete.html')
 
if __name__ == "__main__":
    app.run(debug=True)