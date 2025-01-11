from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm import setup_database, create_session, Directors, Movies  # Подключаем модели из ORM

engine = setup_database("sqlite:///movies.sqlite")
session = create_session(engine)
#Create
def add_director(name):
    new_director = Directors(name = name)
    session.add(new_director)
    session.commit()
    print(f"Director '{name}' added with ID: {new_director.id}")
    return new_director.id

def add_movie(name):
    new_movie = Movies(original_title = name)
    session.add(new_movie)
    session.commit()
    print(f"Movie '{name}' added with ID: {new_movie.id}")
    return new_movie.id
#Read
def get_director_by_id(director_id):
    director = session.query(Directors).filter_by(id=director_id).first()
    if director:
        print(f"Artist:{director.name}")
        return director.name
    else:
        print(f"Artist with ID {director_id} not found")
        return None


def get_movie_by_id(movie_id):
    movie = session.query(Movies).filter_by(id = movie_id).first()
    if movie:
        print(f"Movie:{movie.original_title}")
        return movie.original_title
    else:
        print(f"Movie with ID{movie_id} not found")
        return None

def get_overview_by_id(movie_id):
    movie = session.query(Movies).filter_by(id = movie_id).first()
    if movie:
        print(movie.overview)
        return None
    else:
        return None


def get_director_by_movie(movie_id):
    movie = session.query(Movies).filter_by(id=movie_id).first()
    if movie:
        print(movie.id_director)
        return movie.id_director
    else:
        print(f"Movie with ID{movie_id} not found")
        return None

def get_info_by_id(movie_id):
    movie = session.query(Movies).filter_by(id=movie_id).first()
    if movie:
        print(movie.overview)
        return movie.overview
    else:
        print(f"Movie with ID{movie_id} not found")
        return None



#Update
def update_director(director_id,new_name):
    director = session.query(Directors).filter_by(id = director_id).first()
    if director:
        director.name = new_name
        session.commit()
        print(f"Director ID {director_id} updated to {new_name}")
        return director
    else:
        print(f"Director with ID {director_id} not found")
        return None

def update_movie(movie_id,new_name):
    movie= session.query(Movies).filter_by(id = movie_id).first()
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
    director = session.query(Directors).filter_by(id = director_id).first()
    if director:
        session.delete(director)
        session.commit()
        print(f"Director with ID {director_id} was deleted")
    else:
        print(f"Director with ID {director_id} was not founded")

def delete_movie(movie_id):
    movie = session.query(Movies).filter_by(id = movie_id).first()
    if movie:
        session.delete(movie)
        session.commit()
        print(f"Movie with ID {movie_id} was deleted")
    else:
        print(f"Movie with ID {movie_id} was not founded")





if __name__ == "__main__":
    add_director("New_director")
    add_movie("New_movie")

    get_movie_by_id(43602)
    get_director_by_id(65417)

    update_movie(movie_id,"New_name")
    update_director(director_id,"New_director")

    delete_movie(movie_id)
    delete_director(director_id)

