from flask import Flask, request, render_template
from utils import searches_by_word, searches_by_year, \
    searches_by_rating, searches_by_genre

RATING_CHILDREN = ('G')
RATING_FAMILY = ('G', 'PG', 'PG-13')
RATING_ADULT = ('R', 'NC-17')

app = Flask(__name__)


@app.route("/movie/<title>", methods=["GET"])
def load_movie_page_by_title(title):
    result = searches_by_word(title)
    return result


@app.route("/movie/<year1>/to/<year2>", methods=["GET"])
def load_movies_page_by_year(year1, year2):
    result = searches_by_year(year1, year2)
    return result


@app.route("/movie/rating/children", methods=["GET"])
def load_movies_page_by_rating_children():
    result = searches_by_rating(RATING_CHILDREN)
    return result


@app.route("/movie/rating/family", methods=["GET"])
def load_movies_page_by_rating_family():
    result = searches_by_rating(RATING_FAMILY)
    return result


@app.route("/movie/rating/adult", methods=["GET"])
def load_movies_page_by_rating_adult():
    result = searches_by_rating(RATING_ADULT)
    return result


@app.route("/movie/genre/<genre>", methods=["GET"])
def load_movies_page_by_genre(genre):
    result = searches_by_genre(genre)
    return result


app.run()
