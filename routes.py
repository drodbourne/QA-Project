from flask import render_template, url_for, redirect, request
from application import app, db
from application.model import Game, Review, AddGame, AddReview, UpdateGame, UpdateGameReview

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    all_games = Game.query.all()
    return render_template('home.html', all_games=all_games)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/add_game_info', methods=['GET', 'POST'])
def add_game_info():
    form = AddGame()
    if form.validate_on_submit():
        new_game = Game(game_name=form.game_name.data, 
                    category=form.category.data, 
                    publisher=form.publisher.data)
        db.session.add(new_game)
        db.session.commit()
        return render_template('home.html', all_games=Game.query.all())
    else:
        return render_template('add_game_info.html', form=form)    
        

@app.route('/delete_game_info/<game_name>', methods=['GET', 'POST'])
def delete_game_info(game_name):
    game = Game.query.filter_by(game_name=game_name).first()
    if game:
        db.session.delete(game)
        db.session.commit()
        return render_template('home.html', all_games=Game.query.all())
    return render_template ('home.html', all_games=Game.query.all())

@app.route('/add_game_review', methods=['GET', 'POST'])
def add_game_review():
    form = AddReview()
    form.game_name.choices = [(game.id, game.game_name) for game in Game.query.all()]
    if form.validate_on_submit():
        new_review = Review(rating = form.rating.data,
                            game_id = form.game_name.data, 
                            comments = form.comments.data)
        db.session.add(new_review)
        db.session.commit()
        return render_template('reviewlist.html', all_reviews=Review.query.all())
    else:
        return render_template ('add_game_review.html', form = form)

@app.route('/delete_game_review/<game_id>', methods=['GET', 'POST'])
def delete_game_review(game_id):
    review = Review.query.filter_by(game_id=game_id).first()
    if review:
        db.session.delete(review)
        db.session.commit()
        return render_template ('reviewlist.html', all_reviews=Review.query.all())
    return render_template ('reviewlist.html', all_reviews=Review.query.all())

@app.route('/reviewlist', methods=['GET', 'POST'])
def reviewlist():
    all_reviews = Review.query.all()
    return render_template ('reviewlist.html', all_reviews=all_reviews)

@app.route('/update_game_info/<game_name>', methods=['GET', 'POST'])
def update_game_info(game_name):
    form = UpdateGame()
    update_game_info = Game.query.filter_by(game_name=game_name).first()
    if form.validate_on_submit():
        update_game_info.game_name = form.game_name.data
        update_game_info.category = form.category.data
        update_game_info.publisher = form.publisher.data
        db.session.commit()
        return render_template('home.html', all_games=Game.query.all())
    return render_template ('update_game_info.html', update_game_info=update_game_info, form=form)

@app.route('/update_game_review/<game_id>', methods=['GET', 'POST'])
def update_game_review(game_id):
    form = UpdateGameReview()
    update_game_review = Review.query.filter_by(game_id=game_id).first()
    if form.validate_on_submit():
        update_game_review.rating = form.rating.data
        update_game_review.comments = form.comments.data
        db.session.commit()
        return render_template('reviewlist.html', all_reviews=Review.query.all(), message='Review Updated')
    return render_template ('update_game_review.html', update_game_review=update_game_review, form=form)