
import pytest
from movies_catalogue import tmdb_client

def test_get_single_movie(monkeypatch):
    mock_data = {"id": 123, "title": "Test Movie"}

    class MockResponse:
        def raise_for_status(self):
            pass
        def json(self):
            return mock_data

    def requests_get_mock(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("movies_catalogue.tmdb_client.requests.get", requests_get_mock)
    result = tmdb_client.get_single_movie(123)
    assert result == mock_data

def test_get_single_movie_cast(monkeypatch):
    mock_cast = [{"name": "Actor 1"}, {"name": "Actor 2"}]
    mock_data = {"cast": mock_cast}

    class MockResponse:
        def raise_for_status(self):
            pass
        def json(self):
            return mock_data

    monkeypatch.setattr("movies_catalogue.tmdb_client.requests.get", lambda *a, **kw: MockResponse())
    cast = tmdb_client.get_single_movie_cast(123)
    assert cast == mock_cast

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

    monkeypatch.setattr("movies_catalogue.tmdb_client.requests.get", lambda *a, **kw: MockResponse())
    images = tmdb_client.get_movie_images(123)
    assert images == mock_images