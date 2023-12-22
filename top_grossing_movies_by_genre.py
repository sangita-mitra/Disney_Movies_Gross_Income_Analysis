def top_grossing_movies_by_genre(data, genre, top_n=10):
    """
    Retrieves the top N grossing movies for a specific genre based on inflation-adjusted gross.

    Parameters
    ----------
    data : pandas.DataFrame
        The input DataFrame with movie data.
    genre : str
        The genre for which top grossing movies are to be retrieved.
    top_n : int, optional
        The number of top grossing movies to retrieve (default is 5).

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the top N grossing movies for the specified genre.

    Raises
    ------
    ValueError
        If the specified genre is not present in the DataFrame.

    Examples
    --------
    >>> top_grossing_movies_by_genre(disney_movies_df, 'Adventure')
          movie_title  release_date      genre MPAA_rating   total_gross  inflation_adjusted_gross
    564  Star Wars Ep. VII: The Force Awakens  2015-12-18  Adventure        PG-13     $936,662,225        936662225.00
    17   The Empire Strikes Back               1980-05-21  Adventure        PG        $290,475,067        290475067.00
    ...  # (Top N movies for Adventure genre)

    Notes
    -----
    The function sorts the movies by inflation-adjusted gross in descending order.
    """
    # Check if the specified genre is present in the DataFrame
    if genre not in data["genre"].unique():
        raise ValueError(f"The genre '{genre}' is not present in the DataFrame.")

    # Create a copy of the data to avoid SettingWithCopyWarning
    genre_data = data[data["genre"] == genre].copy()

    # Convert 'inflation_adjusted_gross' to numeric
    genre_data["inflation_adjusted_gross"] = (
        genre_data["inflation_adjusted_gross"]
        .replace("[\$,]", "", regex=True)
        .astype(float)
    )

    # Retrieve the top N grossing movies
    top_movies = genre_data.nlargest(top_n, "inflation_adjusted_gross")

    return top_movies
