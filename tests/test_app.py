from application import app, db
from application.models import Players, Teams, AddTeamForm, AddPlayerForm, UpdateTeamForm, UpdatePlayerForm
from flask import render_template, redirect, url_for, request
from flask_testing import TestCase


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
        team = Teams(team_name="Football Team")
        player = Players(name="Any Name", age=26, position="forward",team_id=1)
        db.session.add(team)
        db.session.add(player)
        db.session.commit()


    def tearDown(self):
    
        db.session.remove()
        db.drop_all()

class TestTeam(TestBase):
    def test_team(self):
        response = self.client.get(url_for('read_team'))
        assert 'Football Team'in response.data.decode()


class TestPlayer(TestBase):
    def test_player(self):
        response = self.client.get(url_for('read_player'))
        assert 'Any Name' in response.data.decode()
        assert '26' in response.data.decode()
        assert 'forward'in response.data.decode()
        assert '1' in response.data.decode()



class TestViews(TestBase):

    def test_home_page(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_create_team(self):
        response = self.client.get(url_for('create_team'))
        self.assertEqual(response.status_code, 200)
      
    def test_update_team(self):
        response = self.client.get(url_for('update_team', id=1))
        self.assertEqual(response.status_code, 200)

    def test_create_player(self):
        response = self.client.get(url_for('create_player', id=1))
        self.assertEqual(response.status_code, 200)
        
    def test_read_player(self):
        response = self.client.get(url_for('read_player', id=1))
        self.assertEqual(response.status_code, 200)

    def test_update_player(self):
        response = self.client.get(url_for('update_player', id=1))
        self.assertEqual(response.status_code, 200)

class TestAdd(TestBase):
    def test_add_team(self):
        response = self.client.post(
            url_for('create_team'),
            data = {'team_name': 'test_team'},
        )
        self.assertEqual(response.status_code, 302)
        assert "create_team" in response.data.decode()

    def test_add_player(self):
        response = self.client.post(
            url_for('create_player'),
            data = {'name': 'add_player' , 'age': 26,'position': 'add_position', 'team_id': 1 },
        )
        self.assertEqual(response.status_code, 200)
        assert "read_player" in response.data.decode()


class TestUpdate(TestBase):
    def test_update_team_info(self):
        response = self.client.post(
            url_for('update_team', id = 1),
            data = {'team_name': 'update_team'},
        )
        self.assertEqual(response.status_code, 302)
        assert "read_team" in response.data.decode()

    def test_update_player(self):
        response = self.client.post(
            url_for('update_player', id = 1),
            data = {'name': 'update_name', 'age': 26 ,'position': 'update_position'},
        )
        self.assertEqual(response.status_code, 302)
        assert "read_player" in response.data.decode()

class TestDelete(TestBase):
    def test_delete_team(self):
        response = self.client.get(
            url_for('delete_team', id = 1))
        self.assertEqual(response.status_code, 302)
        assert "test_team" not in response.data.decode()
    
    def test_delete_player(self):
        response = self.client.get(
            url_for('delete_player', id = 1))
        self.assertEqual(response.status_code, 302)
        assert "add_player" not in response.data.decode()



