from flask import url_for
from app import app, TeamForm, PlayerForm
from flask_testing import TestCase
from models import Team,Players, db


# Create the base class
class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create_all()
        team = Team(name="Football Team")
        player = Players(team_id=1,name="Any Name", age=26, position="forward")
        db.session.add(team)
        db.session.add(player)
        db.session.commit()


    def tearDown(self):
    
        db.session.remove()
        db.drop_all()

class TestTeam(TestBase):
    def test_team(self):
        response = self.client.get(url_for('team'))
        assert 'Football Team'in response.data.decode()

class TestPlayer(TestBase):
    def test_team(self):
        response = self.client.get(url_for('addplayer'))
        assert  1 in response.data.decode()
        assert 'Any Name'in response.data.decode()
        assert 26 in response.data.decode()
        assert 'forward'in response.data.decode()


