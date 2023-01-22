import sqlite3


def load_database():
    with sqlite3.connect("data/netflix.db") as connection:
        return connection


def searches_by_word(word):
    connection = load_database()
    cursor = connection.cursor()
    query = f"""
        SELECT title, country, release_year, listed_in, description
        FROM netflix
        WHERE lower(title) LIKE {word}
        ORDER BY release_year DESC
        """
    cursor.execute(query)
    for row in cursor.fetchall():
        if word in row:
            movie_data_json = {
                    "title": row[0],
                    "country": row[1],
                    "release_year": row[2],
                    "genre": row[3],
                    "description": row[4]
                }
            return movie_data_json


def searches_by_year(year1, year2):
    connection = load_database()
    cursor = connection.cursor()
    query = f"""
            SELECT title, release_year
            FROM netflix
            WHERE release_year BETWEEN {year1} AND {year2}
            ORDER BY release_year DESC
            LIMIT 100
            """
    cursor.execute(query)
    movie_data_list = []
    for row in cursor.fetchall():
        movie_data_json = {
            "title": row[0],
            "release_year": row[1]
        }
        movie_data_list.append(movie_data_json)
    return movie_data_list


def searches_by_rating(rating):
    connection = load_database()
    cursor = connection.cursor()
    query = f"""
            SELECT title, rating, description
            FROM netflix
            WHERE rating LIKE '%{rating[0]}%'
            """
    cursor.execute(query)
    movie_data_list = []
    for row in cursor.fetchall():
        movie_data_json = {
            "title": row[0],
            "rating": row[1],
            "description": row[2]
        }
        movie_data_list.append(movie_data_json)
    return movie_data_list


def searches_by_genre(genre):
    connection = load_database()
    cursor = connection.cursor()
    query = f"""
            SELECT title, description
            FROM netflix
            WHERE lower(listed_in) LIKE '%{genre}%'
            ORDER BY release_year DESC
            LIMIT 10
            """
    cursor.execute(query)
    movie_data_list = []
    for row in cursor.fetchall():
        movie_data_json = {
            "title": row[0],
            "description": row[1]
        }
        movie_data_list.append(movie_data_json)
    return movie_data_list


def searches_by_type(type, year, genre):
    connection = load_database()
    cursor = connection.cursor()
    query = f"""
            SELECT title, description
            FROM netflix
            WHERE lower(listed_in) LIKE '%{genre}%'
            AND lower(type) LIKE '%{type}%'
            AND lower(release_year) LIKE '%{year}%'
            """
    cursor.execute(query)
    movie_data_list = []
    for row in cursor.fetchall():
        movie_data_json = {
            "title": row[0],
            "description": row[1]
        }
        movie_data_list.append(movie_data_json)
    return movie_data_list
