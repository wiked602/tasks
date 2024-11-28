from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import setup_database, create_session, directors, movies  # Подключаем модели из ORM

engine = setup_database("sqlite:///movie.sqlite")
session = create_session(engine)
#Create
def add_director(name):
    new_director = directors(name = name)
    session.add(new_director)
    session.commit()
    print(f"Director '{name}' added with ID: {new_director.id}")
    return new_director.id

def add_movie(name):
    new_movie = movies(original_title = name)
    session.add(new_movie)
    session.commit()
    print(f"Movie '{name}' added with ID: {new_movie.id}")
    return new_movie.id
#Read
def get_director_by_id(director_id):
    director = session.query(directors).filter_by(id=director_id).first()
    if director:
        print(f"Artist:{director.name}")
        return director
    else:
        print(f"Artist with ID {director_id} not found")
        return None

def get_movie_by_id(movie_id):
    movie = session.query(movies).filter_by(id = movie_id).first()
    if movie:
        print(f"Movie:{movie.original_title}")
        return movie
    else:
        print(f"Movie with ID{movie_id} not found")
        return None

#Update
def update_director(director_id,new_name):
    director = session.query(directors).filter_by(id = director_id).first()
    if director:
        director.name = new_name
        session.commit()
        print(f"Director ID {director_id} updated to {new_name}")
        return director
    else:
        print(f"Director with ID {director_id} not found")
        return None

def update_movie(movie_id,new_name):
    movie= session.query(movies).filter_by(id = movie_id).first()
    if movie:
        movie.name = new_name
        session.commit()
        print(f"Movie ID {movie_id} updated to {new_name}")
        return movie
    else:
        print(f"Movie with ID {movie_id} not found")
        return None
#Delete
def delete_director(director_id):
    director = session.query(directors).filter_by(id = director_id).first()
    if director:
        session.delete(director)
        session.commit()
        print(f"Director with ID {director_id} was deleted")
    else:
        print(f"Director with ID {director_id} was not founded")

def delete_movie(movie_id):
    movie = session.query(movies).filter_by(id = movie_id).first()
    if movie:
        session.delete(movie)
        session.commit()
        print(f"Movie with ID {movie_id} was deleted")
    else:
        print(f"Movie with ID {movie_id} was not founded")

if __name__ == "__main__":
    director_id = add_director("New_Director")
    movie_id = add_movie("New_Movie")

    get_movie_by_id(movie_id)
    get_director_by_id(director_id)

    update_movie(movie_id,"New_name2")
    update_director(director_id,"New_director2")

    delete_movie(movie_id)
    delete_director(director_id)

