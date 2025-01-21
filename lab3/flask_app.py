from flask import Flask, render_template, request, jsonify, redirect, url_for
from orm import *

app = Flask(__name__)

engine = setup_database()
session = create_session(engine)


@app.route('/', methods=['GET'])
def index():
    movies = session.query(Movies).all()
    directors = session.query(Directors).all()
    show_movies = request.args.get('show_movies', default='false', type=str) == 'true'
    show_directors = request.args.get('show_directors', default='false', type=str) == 'true'
    return render_template('index.html', movies=movies, directors=directors,show_movies=show_movies, show_directors=show_directors)


@app.route('/movie/<int:movie_id>', methods=['GET'])
def movie_details(movie_id):
    movie = session.query(Movies).get(movie_id)
    if movie:
        return render_template('movie_details.html', movie=movie)
    else:
        return "Movie not found", 404


@app.route('/director/<int:director_id>', methods=['GET'])
def director_details(director_id):
    director = session.query(Directors).get(director_id)
    if director:
        return render_template('director_details.html', director=director)
    else:
         return "Director not found", 404

if __name__ == '__main__':
    app.run(debug=True)