import pandas as pd
import pytest
from top_grossing_movies_by_genre import top_grossing_movies_by_genre


def test_top_grossing_movies_by_genre_valid_genre():
    # Create a sample DataFrame for testing
    data = {
        "movie_title": ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E"],
        "release_date": [
            "2020-01-01",
            "2021-01-01",
            "2019-01-01",
            "2022-01-01",
            "2018-01-01",
        ],
        "genre": ["Adventure", "Adventure", "Drama", "Action", "Comedy"],
        "MPAA_rating": ["PG", "PG-13", "R", "PG", "R"],
        "total_gross": [
            "$100,000,000",
            "$150,000,000",
            "$80,000,000",
            "$120,000,000",
            "$90,000,000",
        ],
        "inflation_adjusted_gross": [
            "$100,000,000",
            "$150,000,000",
            "$80,000,000",
            "$120,000,000",
            "$90,000,000",
        ],
    }
    test_df = pd.DataFrame(data)

    # Test the function with a valid genre
    result = top_grossing_movies_by_genre(test_df, "Adventure", top_n=2)
    assert len(result) == 2, "Expected 2 movies for the Adventure genre"
    assert (
        result["genre"].unique()[0] == "Adventure"
    ), "Expected the genre to be Adventure"


def test_top_grossing_movies_by_genre_sorted():
    # Create a sample DataFrame for testing with sorted inflation-adjusted gross values
    data = {
        "movie_title": ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E"],
        "release_date": [
            "2020-01-01",
            "2021-01-01",
            "2019-01-01",
            "2022-01-01",
            "2018-01-01",
        ],
        "genre": ["Adventure", "Adventure", "Drama", "Action", "Comedy"],
        "MPAA_rating": ["PG", "PG-13", "R", "PG", "R"],
        "total_gross": [
            "$100,000,000",
            "$150,000,000",
            "$80,000,000",
            "$120,000,000",
            "$90,000,000",
        ],
        "inflation_adjusted_gross": [
            "$100,000,000",
            "$150,000,000",
            "$80,000,000",
            "$120,000,000",
            "$90,000,000",
        ],
    }
    test_df = pd.DataFrame(data)

    # Test the function with a valid genre and sorted inflation-adjusted gross
    result = top_grossing_movies_by_genre(test_df, "Adventure", top_n=5)

    # Check if the movies are sorted by inflation-adjusted gross in descending order
    assert result.equals(
        result.sort_values("inflation_adjusted_gross", ascending=False)
    ), "Movies are not sorted by inflation-adjusted gross"
