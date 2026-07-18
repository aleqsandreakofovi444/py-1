from flask import Blueprint, render_template

from app.models.movie_repository import MovieRepository

main_bp = Blueprint("main", __name__)
repository = MovieRepository()


@main_bp.route("/")
def index():
    movies = repository.get_all_movies()
    total_movies = repository.get_movie_count()
    average_duration = repository.get_average_duration()
    return render_template(
        "index.html",
        movies=movies,
        total_movies=total_movies,
        average_duration=average_duration,
    )
