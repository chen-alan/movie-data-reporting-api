from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import extract
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db = SQLAlchemy(app)


# --------------------------- MODELS -------------------------------------------------------
class Movie(db.Model):
    __tablename__ = "movie"
    movie_id = db.Column(db.Integer, primary_key=True)
    original_title = db.Column(db.String)
    release_date = db.Column(db.Date)

class Genre(db.Model):
    __tablename__ = "genre"
    genre_id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String)

class Company(db.Model):
    __tablename__ = "company"
    company_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String)

class MovieGenrePop(db.Model):
    __tablename__ = "movie_genre"
    movie_id = db.Column(db.Integer, db.ForeignKey(Movie.movie_id), primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey(Genre.genre_id))
    popularity = db.Column(db.Float)

class MovieEarning(db.Model):
    __tablename__ = "movie_earning"
    movie_id = db.Column(db.Integer, db.ForeignKey(Movie.movie_id), primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey(Company.company_id))
    revenue = db.Column(db.Integer)
    budget = db.Column(db.Integer)

# ------------------------------------------------------------------------------------------
def valid_input(input):
    # simple check for numeric inputs
    # can add more complex checks if given more time
    return input.isnumeric()

@app.route('/', methods=['GET'])
def index():
    return 'Hiya! Wishing you a happy day :)'


@app.route('/budgets/<company_id>/<year>', methods=['GET'])
def get_company_budget_year(company_id, year):
    if not valid_input(company_id) or not valid_input(year):
        return jsonify({'error': 'Please enter numeric inputs for company_id and year'})

    query = db.session.execute(db.select(Movie, MovieEarning) \
        .join(MovieEarning, Movie.movie_id == MovieEarning.movie_id) \
        .where(MovieEarning.company_id == company_id)
        .filter(extract('year', Movie.release_date) == year))
    
    companyYearBudget = 0

    for _, movieEarning in query:
        companyYearBudget += movieEarning.budget

    return jsonify(companyYearBudget)


@app.route('/revenues/<company_id>/<year>', methods=['GET'])
def get_company_revenue_year(company_id, year):
    if not valid_input(company_id) or not valid_input(year):
        return jsonify({'error': 'Please enter numeric inputs for company_id and year'})

    query = db.session.execute(db.select(Movie, MovieEarning) \
        .join(MovieEarning, Movie.movie_id == MovieEarning.movie_id) \
        .where(MovieEarning.company_id == company_id)
        .filter(extract('year', Movie.release_date) == year))
    
    companyYearRevenue = 0

    for _, movieEarning in query:
        companyYearRevenue += movieEarning.revenue

    return jsonify(companyYearRevenue)


@app.route('/genres/<year>', methods=['GET'])
def get_most_popular_genre_year(year):
    if not valid_input(year):
        return jsonify({'error': 'Please enter numeric inputs for year'})
    
    query = db.session.execute(db.select(Movie, MovieGenrePop) \
        .join(MovieGenrePop, Movie.movie_id == MovieGenrePop.movie_id) \
        .filter(extract('year', Movie.release_date) == year))

    # genreID : sum(popularities)
    genrePopularity = {}    
    
    for _, movieGenrePop in query:
        if movieGenrePop.genre_id in genrePopularity:
            genrePopularity[movieGenrePop.genre_id] += movieGenrePop.popularity
        else:
            genrePopularity[movieGenrePop.genre_id] = movieGenrePop.popularity

    mostPopularGenre = None

    if genrePopularity:
        mostPopularGenreID = sorted(genrePopularity.items(), key=lambda x:x[1])[-1][0]
        mostPopularGenre = Genre.query.get(mostPopularGenreID)

    return jsonify({mostPopularGenre.genre_name : mostPopularGenre.genre_id}) if mostPopularGenre else {}


if __name__ == '__main__':
    app.run(debug=True)