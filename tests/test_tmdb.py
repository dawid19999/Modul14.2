

import pytest
from movies_catalogue import tmdb_client

# -----------------------
# get_single_movie
# -----------------------
def test_get_single_movie(monkeypatch):
    mock_data = {"id": 123, "title": "Test Movie"}

    class MockResponse:
        def raise_for_status(self):
            pass
        def json(self):
            return mock_data

    def requests_get_mock(url, headers):
        # sprawdzamy czy endpoint został poprawnie zbudowany
        assert url == "https://api.themoviedb.org/3/movie/123"
        return MockResponse()

    monkeypatch.setattr("movies_catalogue.tmdb_client.requests.get", requests_get_mock)

    result = tmdb_client.get_single_movie(123)
    assert result == mock_data


# -----------------------
# get_single_movie_cast
# -----------------------
def test_get_single_movie_cast(monkeypatch):
    mock_cast = [{"name": "Actor 1"}, {"name": "Actor 2"}]
    mock_data = {"cast": mock_cast}

    class MockResponse:
        def raise_for_status(self):
            pass
        def json(self):
            return mock_data

    def requests_get_mock(url, headers):
        # sprawdzamy czy endpoint jest z credits
        assert url == "https://api.themoviedb.org/3/movie/123/credits"
        return MockResponse()

    monkeypatch.setattr("movies_catalogue.tmdb_client.requests.get", requests_get_mock)

    cast = tmdb_client.get_single_movie_cast(123)
    assert cast == mock_cast


# -----------------------
# get_movie_images
# -----------------------
def test_get_movie_images(monkeypatch):
    mock_images = {
        "backdrops": [{"file_path": "/abc.jpg"}],
        "posters": [{"file_path": "/poster.jpg"}]
    }

    class MockResponse:
        def raise_for_status(self):
            pass
        def json(self):
            return mock_images

    def requests_get_mock(url, headers):
        # sprawdzamy czy endpoint zawiera images
        assert url == "https://api.themoviedb.org/3/movie/123/images"
        return MockResponse()

    monkeypatch.setattr("movies_catalogue.tmdb_client.requests.get", requests_get_mock)

    images = tmdb_client.get_movie_images(123)
    assert images == mock_images
    assert "backdrops" in images
    assert "posters" in images