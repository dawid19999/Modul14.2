

from flask import Flask, render_template, request
import tmdb_client

app = Flask(__name__)

@app.route('/')
def homepage():
    movie_lists = ['popular', 'now_playing', 'top_rated', 'upcoming']

    
    selected_list = request.args.get('list_type', 'popular')

    
    if selected_list not in movie_lists:
        selected_list = 'popular'

    
    movies = tmdb_client.get_movies_list(list_type=selected_list)

    
    return render_template(
        "homepage.html",
        movies=movies,
        current_list=selected_list,
        movie_lists=movie_lists
    )

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    return render_template("movie_details.html", movie=details, cast=cast)

if __name__ == '__main__':
    tmdb_client.check_api_token()

    app.run(debug=True)