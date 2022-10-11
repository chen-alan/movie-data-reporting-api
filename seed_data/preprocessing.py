import csv
import ast
from curses.ascii import isalnum

INPUT_FILE = 'the-movies-dataset/movies_metadata.csv'

def agg_genres(input_file, output_file):
    """ Aggregates all genres & their ids (genres.csv) """
    with open(input_file, 'r') as input:
        reader = csv.DictReader(input)

        # aggregate a list of genres with their associated ids
        genres = {}

        for row in reader:
            try:
                for genre in ast.literal_eval(row['genres']):
                    name = genre['name']
                    id = genre['id']

                    if name in genres:
                        genres[name].add(id)
                    else:
                        # created a set of ids here for context (wanted to see if
                        # one genre could have multiple ids)
                        # answer: turns out genre to id is 1:1
                        genres[name] = set([id])
            except Exception as ex:
                print('Error in agg_genres(): ', ex)

        # write result to genres.csv (seed for Genre table)
        with open(output_file, 'w') as output:
            fieldnames = ['id', 'genre']
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()

            for genre in genres:
                writer.writerow({'genre': genre, 'id': genres[genre].pop()})


def agg_companies(input_file, output_file):
    """ Aggregates all production companies & their ids (companies.csv) """
    with open(input_file, 'r') as input:
        reader = csv.DictReader(input)

        # aggregate a list of companies with their associated ids
        companies = {}

        for row in reader:
            try:
                for company in ast.literal_eval(row['production_companies']):
                    name = company['name']
                    id = company['id']

                    if name in companies:
                        companies[name].add(id)
                    else:
                        # created a set of ids here for context (wanted to see if
                        # one company could have multiple ids)
                        # answer: turns out company to id is NOT 1:1
                        companies[name] = set([id])
            except Exception as ex:
                print('Error in agg_companies()', ex)

        # write result to genres.csv (seed for Genre table)
        with open(output_file, 'w') as output:
            fieldnames = ['id', 'company']
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()

            for company_name in companies:
                for id in companies[company_name]:
                    writer.writerow({'company': company_name, 'id': id})


def agg_movies(input_file, output_file):
    """ Aggregates all movies with their release year & name """
    with open(input_file, 'r') as input:
        reader = csv.DictReader(input)

        # aggregate a list of movies with their associated release year & name
        movies = {}

        for row in reader:
            try:
                original_title = row['original_title']
                release_date = row['release_date']
                movie_id = row['id']

                if movie_id.isnumeric(): 
                    movies[movie_id] = {
                        'movie_id': movie_id,
                        'original_title': original_title, 
                        'release_date': release_date
                    }
            except Exception as ex:
                print('Error in agg_movies()', ex)

        # write result to movies.csv (seed for Movie table)
        with open(output_file, 'w') as output:
            fieldnames = ['movie_id', 'original_title', 'release_date']
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()

            for movie_id in movies:
                writer.writerow(movies[movie_id])


def agg_movie_genre_popularities(input_file, output_file):
    """ Aggregates all movies with their genres & popularity """
    with open(input_file, 'r') as input:
        reader = csv.DictReader(input)

        # aggregates a list of movies, their genres, and their popularity
        movie_genre_popularities = {}

        for row in reader:
            try:
                for genre in ast.literal_eval(row['genres']):
                    movie_id = row['id']
                    genre_id = genre['id']
                    popularity = row['popularity']

                    if movie_id.isnumeric():
                        movie_genre_popularities[movie_id] = {
                            'movie_id': movie_id,
                            'genre_id': genre_id,
                            'popularity': popularity
                        }
            except Exception as ex:
                print('Error in agg_movie_genre_popularities()', ex)
        
        # write result to movie_genres.csv (seed for MovieGenrePopularity table)
        with open(output_file, 'w') as output:
            fieldnames = ['movie_id', 'genre_id', 'popularity']
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()

            for movie_id in movie_genre_popularities:
                writer.writerow(movie_genre_popularities[movie_id])


def agg_movie_earnings(input_file, output_file):
    """ Aggregates all movies with their production companies, revenue, and budget """
    with open(input_file, 'r') as input:
        reader = csv.DictReader(input)

        # aggregates a list of movies, their production companies, revenue, and budget
        movie_earnings = {}

        for row in reader:
            try:
                for company in ast.literal_eval(row['production_companies']):
                    movie_id = row['id']
                    company_id = company['id']
                    revenue = row['revenue']
                    budget = row['budget']

                    if movie_id.isnumeric():
                        movie_earnings[movie_id] = {
                            'movie_id': movie_id,
                            'company_id': company_id,
                            'revenue': revenue,
                            'budget': budget
                        }
            except Exception as ex:
                print('Error in agg_movie_earnings()', ex)
        
        # write result to movie_earnings.csv (seed for MovieEarnings)
        with open(output_file, 'w') as output:
            fieldnames = ['movie_id', 'company_id', 'revenue', 'budget']
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()

            for movie_id in movie_earnings:
                writer.writerow(movie_earnings[movie_id])

def run():
    # build seed data for the Genre table (genres.csv)
    print('Building seed for Genre table(genres.csv)...')
    agg_genres(INPUT_FILE, 'genres.csv')

    # build seed data for the Company table (companies.csv)
    print('Building seed for Company table(companies.csv)...')
    agg_companies(INPUT_FILE, 'companies.csv')

    # build seed data for the Movie table (movies.csv)
    print('Building seed for Movie table(movies.csv)...')
    agg_movies(INPUT_FILE, 'movies.csv')

    # build seed data for MovieGenrePopularity table (movie-genre-popularities.csv)
    print('Building seed for MovieGenrePopularity table(movie-genre-popularities.csv)...')
    agg_movie_genre_popularities(INPUT_FILE, 'movie-genre-popularities.csv')

    # build seed data for MovieEarning table (movie-earnings.csv)
    print('Building seed for MovieEarning table(movie-earnings.csv)...')
    agg_movie_earnings(INPUT_FILE, 'movie-earnings.csv')

run()